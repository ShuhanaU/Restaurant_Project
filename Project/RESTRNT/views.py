from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required




def index(request):
    Home_image=Post.objects.filter(category_id=1)
    Slider=Post.objects.filter(category_id=2)
    offers=Post.objects.filter(category_id=3)
    Foodsection=Post.objects.filter(category_id=4)
    product_category=ProductCategory.objects.all()
    product=Product.objects.all()
    # about_section=Post.objects.get(category_id=5)
    customer_review=Post.objects.filter(category_id=6)
    data={
        'Home_image':Home_image,
        'Slider':Slider,
        'offers':offers,
        'Foodsection':Foodsection,
        'productcategories':product_category,
        'products':product,
        # 'about_section':about_section,
        'customer_review':customer_review,
    }
    return render(request,"index.html",data)

def menu(request):
    product_category=ProductCategory.objects.all()
    product=Product.objects.all()
    data={
        'productcategories':product_category,
        'products':product,
    }
    return render(request,"menu.html",data)


def about(request):
    # about_section=Post.objects.get(category_id=5)
    # data={
    #     'about_section':about_section,
    # }
    return render(request,"about.html")

@login_required
def book(request):
    user_id=request.user.id
    user_profile=Profile.objects.get(user_id=user_id)
    data={
        
         'log_det1':request.user,
         'log_det2':user_profile,
      }
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        phonenumber=request.POST.get("phonenumber")
        noOfperson=request.POST.get("nop")
        date=request.POST.get("date")
        book=BookaTable(username=username,email=email,phonenumber=phonenumber,noOfperson=noOfperson,date=date,user_id=user_id)
        book.save()
        return JsonResponse({'success':True,'message':'Booked successfully'})
    return render(request,"book.html",data)

def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        message=request.POST["message"]
        feedback=Feedback(name=name,email=email,message=message)
        feedback.save()
        return redirect("index")
    return render(request,"contact.html")

def userLogin(request):
    if request.method=="POST":
     username=request.POST.get("username")
     password=request.POST.get("password")
     user=authenticate(request,username=username,password=password)
     if user is not None:
      login(request,user)
      return JsonResponse({'success': True,'message':"Login success",'redirect':'/profile'})
     else:
        return JsonResponse({'success': False,'message':"Email or password is incorrect"})
    return render(request,"Login.html")

@login_required
def Userprofile(request):
     about_section=Post.objects.filter(category_id=5)
     user_id=request.user.id
     user_profile=Profile.objects.get(user_id=user_id)
     data={
        'about_section':about_section,
        'log_det1':request.user,
         'log_det2':user_profile,
      }
     
     return render(request,"profile.html",data)

def register(request):
    Home_image=Post.objects.filter(category_id=1)
    data={
        'Home_image':Home_image,
    }
    if request.method=='POST':
        username=request.POST.get("username")
        phonenumber=request.POST.get("phonenumber")
        place=request.POST.get("place")
        password=request.POST.get("password")
        email=request.POST.get("email")
        image=request.FILES.get("image")
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
          return JsonResponse({'error':'Username or email is already in use'},status=400)

        user=User(username=username,email=email)
        user.set_password(password)
        user.save()
        profile=Profile(user=user,phonenumber=phonenumber,place=place,image=image)
        profile.save()
        return JsonResponse({'message':'User registered successfully'})
    return render(request,"register.html",data)

@login_required
def Logout(request):
  logout(request)
  return redirect('index') 

@login_required
def update(request):
    user_id=request.user.id
    user_profile=Profile.objects.get(user_id=user_id)
    data={
        
         'log_det1':request.user,
         'log_det2':user_profile,
      }
     
    if request.method=='POST':
     username=request.POST["username"]
     phonenumber=request.POST["phonenumber"]
     place=request.POST["place"]
     email=request.POST["email"]
     ids=request.user.id
     profile=Profile.objects.get(user_id=ids)
     user=profile.user
     user.username=username
     user.email=email
     user.save()
     profile.phonenumber=phonenumber
     profile.place=place

     if 'image' in request.FILES:
        profile.image=request.FILES['image']
        
     profile.save()
     return redirect('profile')
    return render(request,'update.html',data)

def view_cart(request):
    cart=request.session.get('cart',{})
    cart_items=[{'id':key,'quantity':value} for key,value in cart.items() if key.isdigit()]
    product_ids=[item['id'] for item in cart_items]
    products=Product.objects.filter(id__in=product_ids)
    cart_count=get_cart_count(request)
    print(cart_items)

    for item in cart_items:
        product = products.get(id=item['id'])
        item['product']=product
        item['total_price']=product.prdctprc * item['quantity']

    subtotal = sum(item['total_price'] for item in cart_items)
    subtotal_formatted = '{:.2f}'.format(subtotal)

    context={
        'cart_items':cart_items,
        'cart_count':cart_count,
        'subtotal':subtotal_formatted
    }

    return render(request, 'cart.html',context)

def add_to_cart(request):
    if request.method=='POST':
        item_id=request.POST.get('item_id')
        quantity=int(request.POST.get('quantity',1))

        #add to cart in session
        cart=request.session.get('cart',{})
        if item_id in cart:
            cart[item_id]+=quantity
        else:
            cart[item_id]=quantity
        request.session['cart'] = cart

        #calculate the total cart count
        cart_count = sum(cart.values())

        return JsonResponse({
            'success':True,
            'cart_count':cart_count
        })
    return JsonResponse({'success':False,'error':'Invalid method'})

def get_cart_count(request):
    cart = request.session.get('cart',{})
    return sum(cart.values())



# def cart(request):
#     return render(request,'cart.html')

#for removing cart item
def remove_from_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]
            request.session['cart'] = cart
            return JsonResponse({'success': True, 'message': 'Item removed successfully!'})

        return JsonResponse({'success': False, 'message': 'Item not found in cart!'})

    return JsonResponse({'success': False, 'message': 'Invalid method'})

#for editing cart item

def edit_cart_item(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        new_quantity = int(request.POST.get('new_quantity'))

        cart = request.session.get('cart', {})
        if item_id in cart:
            cart[item_id] = new_quantity
            request.session['cart'] = cart

            product = Product.objects.get(id=item_id)
            updated_total_price = product.prdctprc * new_quantity

            return JsonResponse({'success': True, 'message': 'Quantity updated successfully!','updated_total_price': "{:.2f}".format(updated_total_price)})

        return JsonResponse({'success': False, 'message': 'Item not found in cart!'})

    return JsonResponse({'success': False, 'message': 'Invalid method'})

def checkout(request):

    cart=request.session.get('cart',{})
    cart_items=[{'id':key,'quantity':value} for key,value in cart.items() if key.isdigit()]
    product_ids=[item['id'] for item in cart_items]
    products=Product.objects.filter(id__in=product_ids)
    cart_count=get_cart_count(request)


    for item in cart_items:
        product = products.get(id=item['id'])
        item['product']=product
        item['total_price']=product.prdctprc * item['quantity']

    subtotal = sum(item['total_price'] for item in cart_items)
    subtotal_formatted = '{:.2f}'.format(subtotal)

    context={
        'cart_items':cart_items,
        'cart_count':cart_count,
        'subtotal':subtotal_formatted,
        
    }

    if request.method=='POST':
     full_name=request.POST["full_name"]
     address=request.POST["address"]
     phone=request.POST["phone"]
     city=request.POST["city"]
     pin_code=request.POST["pin_code"]
     
    
     order=Shipping(
        full_name=full_name,
        address=address,
        phone=phone,
        city=city,
        pin_code=pin_code,
     )
     order.save()


     user_order_obj=UserOrder(
        user=request.user,
        subtotal=subtotal,
        shipping_details=order,
     )
     user_order_obj.save()
     pid_list=request.POST.getlist('pid[]')
     quantity_list=request.POST.getlist('quantity[]')
    
    # loop through the lists and populate the cart dictionary
     for pid,quantity in zip(pid_list,quantity_list):
        product=Product.objects.get(id=int(pid))
     cartitem_obj=CartItem(
        order_id=order.id,
        product=product,
        quantity=int(quantity)
     )
     cartitem_obj.save()

     request.session['cart']={}
     response_data={'success':True}
     return JsonResponse(response_data)
    return render(request, 'checkout.html',context)

def singleproduct(request,item_id):
     product=get_object_or_404(Product,id=item_id)
     product_categories=ProductCategory.objects.filter(product=product)
     data={
      'product':product,
      'product_categories':product_categories,
      }
     return render(request,'singleproduct.html',data)

def addproduct(request):
    allproduct=ProductCategory.objects.all()
    if request.method == 'POST':
        product_category_id = request.POST.get('product_category')  # Corrected the variable name
        selected_product_category = get_object_or_404(ProductCategory, id=product_category_id)
        if selected_product_category is None:
            return JsonResponse({'error': 'Invalid product category'})
        productname = request.POST.get('title')
        prdctprc = request.POST.get('price')
        desc = request.POST.get('description')
        desc2=request.POST.get('desc2')
        img = request.FILES['image']
        
        product = Product(
            category=selected_product_category,  # Use the selected_product_category
            productname=productname,
            prdctprc=prdctprc,
            desc=desc,
            desc2=desc2,
            img=img,
        )
        product.save()
   
        return redirect('menu')
    
    return render(request, 'addproduct.html', {'allproduct':allproduct })
# Create your views here.
  