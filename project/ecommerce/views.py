from django.http.response import HttpResponse
from django.shortcuts import render
import csv
import requests

from user.models import crop,contract

from user.models import wishlist
from user.models import location
from django.contrib import messages
# Create your views here.
from django.core import serializers


def mycontracts(request):
    if request.user.is_authenticated:
        if request.user.isFarmer:
            messages.info(request, 'Please Register as a Buyer to view this page.')
            return render( request, 'ecommerce/error_msg.html')
        
        else:
            try:
                address = location.objects.get(user=request.user)
            
                if request.POST:
                    print("bbbbbbb")
                    # name = request.POST.get('name')
                    if request.POST.get('submit') == "add_new_crop":
                        crop_name = request.POST['crop_name']
                        price = request.POST['price']
                        quantity = request.POST['quantity']
                        date = request.POST['date']
                    
                        # photo = request.FILES['photo']
                        new_crop = contract( user=request.user, crop_name = crop_name, price=price, quantity=quantity, date=date)
                        new_crop.save()
                        print(new_crop)
                    # elif request.POST.get('submit') == "edit_crop":

                    #     return 
                    elif request.POST.get('submit') == "delete_crop":
                        print("asdfsad")
                        contract.objects.filter(id=request.POST.get('crop_id')).delete()

                    elif request.POST.get('submit') == "edit_crop":
                        
                        crop_name = request.POST['crop_name']
                        price = request.POST['price']
                        quantity = request.POST['quantity']
                        date = request.POST['date']
                        # photo = request.FILES['photo']
                        contract.objects.filter(id=request.POST.get('crop_id')).update(crop_name=crop_name,price=price,quantity=quantity, date=date)
                        
                context = {}
                # context['crop'] = {'sdf','asd','lol'}
                data=[]
                # data = pd.read_csv("fertilizer.csv")
                with open('home/fertilizer.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row[1])
                data.sort()
                context['crop'] = data

                crops_added = contract.objects.filter(user=request.user)
                
                return render( request, 'ecommerce/view_your_added_contracts.html', {'crop':data,'crops_added': crops_added })
            
            except:
                messages.info(request, 'Please complete your profile to view this page.')
                return render( request, 'ecommerce/error_msg.html')

    else:
        messages.info(request, 'Please Login/Register as a Buyer to view this page.')
        return render( request, 'ecommerce/error_msg.html')
    

def viewcontracts(request):
    # return( request, 'ecommerce/view_your_added_crops.html')
    
    if request.user.is_authenticated:
        all_crops = contract.objects.filter()

        data1=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/commodity.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != "All":
                    data1.append(row[0])
        data1.sort()
        # context['commodity'] = data1
        data2=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/state.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data2.append(row[0])
        data2.sort()
        # context['state'] = data2

        data3=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/district.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data3.append(row[0])
        data3.sort()
        
        return render( request, 'ecommerce/view_all_contracts.html' , { 'all_crops':all_crops, 'commodity':data1, 'state':data2, 'district': data3} )
    else:
        messages.info(request, 'Please Login/Register to view this page.')
        return render( request, 'ecommerce/error_msg.html')


def mycrops(request):
    if request.user.is_authenticated:
        if request.user.isFarmer:
            try:
                address = location.objects.get(user=request.user)
            
                if request.POST:
                    print("bbbbbbb")
                    # name = request.POST.get('name')
                    if request.POST.get('submit') == "add_new_crop":
                        crop_name = request.POST['crop_name']
                        price = request.POST['price']
                        quantity = request.POST['quantity']
                        photo = request.FILES['photo']
                        new_crop = crop( user=request.user, crop_name = crop_name, price=price, quantity=quantity, photo=photo)
                        new_crop.save()
                        print(new_crop)
                    # elif request.POST.get('submit') == "edit_crop":

                    #     return 
                    elif request.POST.get('submit') == "delete_crop":
                        print("asdfsad")
                        crop.objects.filter(id=request.POST.get('crop_id')).delete()

                    elif request.POST.get('submit') == "edit_crop":
                        
                        crop_name = request.POST['crop_name']
                        price = request.POST['price']
                        quantity = request.POST['quantity']
                        # photo = request.FILES['photo']
                        crop.objects.filter(id=request.POST.get('crop_id')).update(crop_name=crop_name,price=price,quantity=quantity)
                        
                        # return 
                context = {}
                # context['crop'] = {'sdf','asd','lol'}
                data=[]
                # data = pd.read_csv("fertilizer.csv")
                with open('home/fertilizer.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row[1])
                data.sort()
                context['crop'] = data

                crops_added = crop.objects.filter(user=request.user)
                
                return render( request, 'ecommerce/view_your_added_crops.html', {'crop':data,'crops_added': crops_added })
            
            except:
                messages.info(request, 'Please complete your profile to view this page.')
                return render( request, 'ecommerce/error_msg.html')
        
        else:
            messages.info(request, 'Please Register as a Farmer to view this page.')
            return render( request, 'ecommerce/error_msg.html')
            # return HttpResponse("Please Register as a Farmer to upload your crops")
    else:
        messages.info(request, 'Please Login/Register as a Farmer to view this page.')
        return render( request, 'ecommerce/error_msg.html')
    

def viewcrops(request):
    # return( request, 'ecommerce/view_your_added_crops.html')
    
    if request.user.is_authenticated:
        all_crops = crop.objects.filter()
        # all_crops = crop.objects.raw("select * from user_crop where user_crop.id != user_wishlist.crop")
        # print("xxxxxxxxxxxxxxxxxx",all_crops2,all_crops)
        if request.POST:
            crop_id = request.POST['crop_id']
            wished = wishlist( user=request.user, crop = crop.objects.get(pk=crop_id) )
            wished.save()
        # for p in crop.objects.raw('SELECT * FROM myapp_crop'):
        #     print(p)
        wish_list = wishlist.objects.filter(user=request.user)
        # wish_list = serializers.serialize("json", wishlist.objects.filter(user=request.user))
        print(wish_list)
        for wish in wish_list:
            # print(wish)
            # cropp = crop.objects.get()
            # print(wish.crop.id)
            all_crops = all_crops.exclude(pk=wish.crop.id)
        # for pair in wish_list:
        #     if pair.crop in all_crops:

        data1=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/commodity.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != "All":
                    data1.append(row[0])
        data1.sort()
        # context['commodity'] = data1
        data2=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/state.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data2.append(row[0])
        data2.sort()
        # context['state'] = data2

        data3=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/district.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data3.append(row[0])
        data3.sort()
        # context['district'] = data3
        
        return render( request, 'ecommerce/view_all_crops.html' , { 'all_crops':all_crops, 'wished_crop':wish_list, 'commodity':data1, 'state':data2, 'district': data3} )
    else:
        messages.info(request, 'Please Login/Register to view this page.')
        return render( request, 'ecommerce/error_msg.html')


def mywishlist(request):

    if request.user.is_authenticated:
        wish_list = wishlist.objects.filter(user=request.user)
        
        # if request.POST:
        #     if request.POST.get('submit') == "add_to_wishlist":
        #         crop_id = request.POST.get('crop_id')
        #         wished = wishlist( user=request.user, crop = crop.objects.get(pk=crop_id) )
        #         wished.save()
                
        if request.POST.get('submit') == "remove_crop":
                print("asdfsad")
                wishlist.objects.filter(id=request.POST.get('wish_id')).delete()
        return render( request, 'ecommerce/list_of_wish.html', { 'wishlist':wish_list } )
    else:
        messages.info(request, 'Please Login/Register to view this page.')
        return render( request, 'ecommerce/error_msg.html')


def sellcrops(request):
    print("bbbbbbb")
    if request.user.is_authenticated:
        if request.POST:
            print("bbbbbbb")
            # name = request.POST.get('name')
            if request.POST.get('submit') == "add_new_crop":
                crop_name = request.POST['crop_name']
                price = request.POST['price']
                quantity = request.POST['quantity']
                photo = request.FILES['photo']
                new_crop = crop( user=request.user, crop_name = crop_name, price=price, quantity=quantity, photo=photo)
                new_crop.save()
                print(new_crop)
            # elif request.POST.get('submit') == "edit_crop":

            #     return 
            elif request.POST.get('submit') == "delete_crop":
                print("asdfsad")
                crop.objects.filter(id=request.POST.get('crop_id')).delete()

            elif request.POST.get('submit') == "edit_crop":
                
                crop_name = request.POST['crop_name']
                price = request.POST['price']
                quantity = request.POST['quantity']
                photo = request.FILES['photo']
                crop.objects.filter(id=request.POST.get('crop_id')).update(crop_name=crop_name,price=price,quantity=quantity,photo=photo)
                
                # return 
        context = {}
        # context['crop'] = {'sdf','asd','lol'}
        data=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/fertilizer.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row[1])
        data.sort()
        context['crop'] = data

        crops_added = crop.objects.filter(user=request.user)
        all_crops = crop.objects.filter()
        return render( request, 'ecommerce/sell.html', {'crop':data, 'crops_added': crops_added ,"all_crops":all_crops })
    else:
        return HttpResponse("sorry")


def mandi(request):
    context = {}
    # context['crop'] = {'sdf','asd','lol'}
    data1=[]
    # data = pd.read_csv("fertilizer.csv")
    with open('home/commodity.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data1.append(row[0])
    data1.sort()
    context['commodity'] = data1


    data2=[]
    # data = pd.read_csv("fertilizer.csv")
    with open('home/state.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data2.append(row[0])
    data2.sort()
    context['state'] = data2

    data3=[]
    # data = pd.read_csv("fertilizer.csv")
    with open('home/district.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data3.append(row[0])
    data3.sort()
    context['district'] = data3



    return render( request, 'ecommerce/mandi.html',context)

def mandipred(request):
    if request.POST:
        commodity = request.POST['commodity']
        state = request.POST['state']
        district= request.POST['district']


        print(state)
        print(district)
        print(commodity)
        
       
            
       

        #url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        url=f'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd00000105e2ba56e600420b6fbbdfd39f5af462&format=json&offset=0&limit=1000'
        response = requests.get(url)
        data = response.json()
        records = data['records']
        final =[]

        for i in records:
            if i['commodity'] == commodity:
                if i['state'] == state:
                    if i['district'] == district:
                        final.append(i)
                    elif district == 'All':
                        final.append(i)    
                
                elif state == 'All':
                    final.append(i)        
                
            elif commodity == 'All':
                if i['state'] == state:
                    if i['district'] == district:
                        final.append(i)
                    elif district == 'All':
                        final.append(i)
        
                elif state == 'All':
                    final.append(i)

        records=final  

        print(len(records))
        a=len(records)
        if a !=0:
            context = {'records' : records, 'commodity': commodity}
            return render( request, 'ecommerce/mandi_result_table.html', context)

        else:
            #number="empty"
            #context = {'number' : number}
            return render( request, 'ecommerce/mandi_result_sorry.html')    



def farmerpro(request):
    # return HttpResponse("HHH")
    # far_id = request.POST['farmer_id']
    first = request.POST['first']
    last = request.POST['last']
    phone = request.POST['phone']
    state = request.POST['state']
    city = request.POST['city']
    # address = location.objects.filter(user=far_id)
    print(first)
    print(last)
    context = {'first_name':first, 'last_name':last, 'phone':phone, 'state':state, 'city':city}
    print("aaaaaaa")
    # print(address)
    return render( request, 'ecommerce/farm_profile.html', context)


def buyerpro(request):
    # return HttpResponse("HHH")
    # far_id = request.POST['farmer_id']
    first = request.POST['first']
    last = request.POST['last']
    phone = request.POST['phone']
    state = request.POST['state']
    city = request.POST['city']
    # address = location.objects.filter(user=far_id)
    print(first)
    print(last)
    context = {'first_name':first, 'last_name':last, 'phone':phone, 'state':state, 'city':city}
    print("aaaaaaa")
    # print(address)
    return render( request, 'ecommerce/buyer_profile.html', context)