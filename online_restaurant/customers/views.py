from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# Create your views here.

sys.path.append('..')

from chefs.models import dish,dish_chef,chef
from .models import eat_in
from .models import take_away

def menu(request):
    return render(request, "customers/menu.html")


def order(request):
    try:
        if request.method == 'GET':
            # 获取所有的数据
             # 分页实现部分
            all_items = dish.objects.all().order_by('dno')

                # 设置每页显示的数据数量
            items_per_page = 4
            paginator = Paginator(all_items, items_per_page)

                # 获取当前页数
            page = request.GET.get('page')
            items = paginator.get_page(page)
                # 分页实现部分
            return render(request, 'customers/order.html', {'items': items})
        if request.method == 'POST':
            dno = request.POST["item_dno"]
            comments = request.POST['comments']
            if 0 < int(request.POST["table_name"]) <= 8:
                tno = request.POST["table_name"]
                last_one = eat_in.objects.all().order_by('eat_in_no').last().eat_in_no
                eat_in_no = 1
                if last_one:
                    eat_in_no = last_one + 1
                temp_eat_in = eat_in(eat_in_no=eat_in_no, tno=tno, dno=dno, comments=comments, finished=False)
                temp_eat_in.save()
                prompt = f'table {tno} has ordered dish {dno} eating in'
                return render(request,'customers/order_finished.html',{'context': prompt})
            if int(request.POST["table_name"]) == 0:
                last_one = take_away.objects.all().order_by('take_away_no').last().take_away_no
                take_away_no = 1
                if last_one:
                    take_away_no = last_one + 1
                temp_take_away = take_away(take_away_no=take_away_no, dno=dno, comments=comments,finished=False)
                temp_take_away.save()
                prompt = f'{take_away_no} customer has ordered dish {dno} taking away'
                return render(request, 'customers/order_finished.html', {'context': prompt})
            # 分页实现部分
            return render(request, 'customers/order_error.html',{'error': 'fraud order'})
    except Exception as e:
        return render(request, 'customers/order_error.html', {'error': e})


def product(request):
    try:
        if request.method == 'GET':
            # 获取所有的数据
            # 分页实现部分
            items_list_1 = eat_in.objects.filter(finished=False).order_by('eat_in_no')
            items_list_2 = take_away.objects.filter(finished=False).order_by('take_away_no')
            # 设置每页显示的数据数量
            items_per_page = 4
            paginator1 = Paginator(items_list_1, items_per_page)
            paginator2 = Paginator(items_list_2, items_per_page)
            # 获取当前页数
            page_1 = request.GET.get('page_1', 1)
            page_2 = request.GET.get('page_2', 1)

            try:
                # 获取当前页的对象列表
                items_1 = paginator1.page(page_1)
                items_2 = paginator2.page(page_2)
            except PageNotAnInteger:
                # 如果页码不是整数，返回第一页
                items_1 = paginator1.page(1)
                items_2 = paginator2.page(1)
            except EmptyPage:
                # 如果页码超出范围，返回最后一页
                items_1 = paginator1.page(paginator1.num_pages)
                items_2 = paginator2.page(paginator2.num_pages)

            return render(request, 'customers/product.html', {'items_1': items_1, 'items_2': items_2})
        if request.method == 'POST':
            if "cook" in request.POST:
                dno = request.POST["item_dno"]
                cno = request.POST['cno']
                prompt = ""
                if chef.objects.filter(cno=cno) and dish_chef.objects.filter(cno=cno,finished=False).count() < 6:
                    last_one = dish_chef.objects.all().order_by('df_no').last()
                    df_no = 1
                    if last_one:
                        df_no = last_one.df_no + 1
                    temp_df = dish_chef(df_no=df_no, dno=dno, cno=cno, finished=False)
                    temp_df.save()
                    prompt = f"df_no: {df_no} join product queue"
                return render(request, 'customers/return.html', {'context': prompt})
            if "finish" in request.POST:
                dno = request.POST["item_dno"]
                cno = request.POST['cno']
                prompt = ""
                if chef.objects.filter(cno=cno):
                    dish_chef.objects.filter(dno=dno,cno=cno,finished=False).update(finished=True)
                    if "item_take_away_no" in request.POST:
                        take_away_no = request.POST["item_take_away_no"]
                        take_away.objects.filter(take_away_no=take_away_no).update(finished=True)
                        prompt = f"{take_away_no} take away finished"
                    if "item_eat_in_no" in request.POST:
                        eat_in_no = request.POST["item_eat_in_no"]
                        eat_in.objects.filter(eat_in_no=eat_in_no).update(finished=True)
                        prompt = f"{eat_in_no} eat in finished"
                return render(request,'customers/return.html',{'context': prompt})
    except Exception as e:
        return render(request,'customers/product_error.html', {'error': e})