from tkinter import *
import mysql.connector
import random
from datetime import date
print("\t","*"*75)
print("\t\t🆂 🅷 🅾 🅿  🆉 🅴 🅽   - 🅾  🅽 🅻 🅸 🅽 🅴    🆁 🅴 🆃 🅰  🅸 🅻    🆂 🆃 🅾  🆁 🅴")
print("\t","*"*75)
 

'''done - Addc(),Addp(),Modifyc(),Modifyp(),deletec(),deletep(),stodisplay(),stograph(),sale(),giveawaydeals()'''

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="group62")
cur=conn.cursor()


"""Admin portal"""
def Addc():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="group62")
    cur=conn.cursor()
    print("")
    print("\t\t\t", "-"*4, "Category", "-"*4)
    print("\t\t", "_"*41)
    # try:
    # Id = input("\t\t  Enter Category Id\t     :")
    Name = input("\t\t  Enter Category Name\t     :")
    Desc = input("\t\t  Enter Description\t     :")
    sql = "insert into category values ({},'{}','{}')".format(
        "NULL", Name, Desc)
    cur.execute(sql)
    cur.execute("commit")
    print("")
    print("\t\t\t", "-"*32, sep="")
    print("\t\t\t|Category Inserted SuccessFully|")
    print("\t\t\t", "-"*32, sep="")
    # except:
    #     print()
    #     print("\t\t  ","*"*38)
    #     print("\t\t   *Category Id already exist, Try again*")
    #     print("\t\t  ","*"*38)
    #     print("\t\t", "_"*41)
    #     Addc()

def Addp():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="group62")
    cur = conn.cursor()
    print("")
    print("\t\t\t", "-"*4, "Adding Product", "-"*4)
    print("\t\t", "_"*41)
    try:
        # Id = input("\t\t  Enter Product Id\t     :")
        CId = input("\t\t  Enter Category Id\t     :")
        if CId.isdigit():
            Name = input("\t\t  Enter Product Name\t     :")
            qty = input("\t\t  Enter Qty\t\t     :")
            price = input("\t\t  Enter Price\t\t     :")
            compname = input("\t\t  Enter Company Name\t     :")
            Desc = input("\t\t  Enter Description\t     :")
            dom = input("\t\t  Enter Dom\t\t:")
            doe = input("\t\t  Enter Doe\t\t:")
            sql = "insert into product values ({},{},'{}',{},{},'{}','{}','{}',{})".format(
                "NULL", CId,Name, qty, price, compname, Desc, dom, doe)
            cur.execute(sql)
            cur.execute("commit")
            print("")
            print("\t\t\t", "-"*31, sep="")
            print("\t\t\t|Product Inserted SuccessFully|")
            print("\t\t\t", "-"*31, sep="")
        else: 
            print("\t\t\tInvalid Id, should be a Integer")
    except:
        print("\t\t\tCategory Id does not exist, Try again")
        Addp()

def modifyc():
    print("")
    print("\t\t\t","-"*4,"Modifying Category","-"*4)
    while True:
        print("\t\t","_"*41)
        print("\t\t\tChoice\t\t|\tAction")
        print("\t\t","_"*41)
        print("\t\t\t1.\t\t|\tCategory Name")
        print("\t\t\t2.\t\t|\tDescription")
        print("\t\t\t3.\t\t|\tExit")
        print("\t\t","_"*41)
        x=int(input("\t\t\tEnter Your Choice\t:"))
        print("\t\t","_"*41)
        if x==1:
            Name=input("\t\t  Enter Category Id To Be Modified\t:")
            if Name.isdigit():
                query="select catid from category where catid={}".format(Name)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Namex=input("\t\t  Enter New Category Name\t\t:")
                    sql="update category set catname='{}' where catid={}".format(Namex,Name)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else: 
                print("Invalid Id, should be a Integer")
        elif x==2:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select catid from category where catid={}".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Price=input("\t\t  Enter New Description\t\t:")
                    sql="update category set Description='{}' where catid={}".format(Price,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else: 
                print("Invalid Id, should be a Integer")
        else:

            break
            

def modifyp():
    print("")
    print("\t\t\t","-"*4,"Modifying product","-"*4)
    while True:
        print("\t\t","_"*41)
        print("\t\t\tChoice\t\t|\tAction")
        print("\t\t","_"*41)
        print("\t\t\t1.\t\t|\tProduct_Name")
        print("\t\t\t2.\t\t|\tQuantity")
        print("\t\t\t3.\t\t|\tPrice")
        print("\t\t\t4.\t\t|\tCompanyName")
        print("\t\t\t5.\t\t|\tdom")
        print("\t\t\t6.\t\t|\tdoe")
        print("\t\t\t7.\t\t|\tExit")
        print("\t\t","_"*41)
        x=int(input("\t\t\tEnter Your Choice\t:"))
        print("\t\t","_"*41)
        if x==1:
            Name=input("\t\t  Enter Id To Be Modified\t:")
            if Name.isdigit():
                query="select pid from product where pid='{}'".format(Name)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Namex=input("\t\t  Enter New Name\t\t:")
                    sql="update product set pname='{}' where pname='{}'".format(Name,Namex)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        elif x==2:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select pid from product where pid='{}'".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    qty=input("\t\t  Enter New Qty\t\t:")
                    sql="update product set qty={} where pid='{}'".format(qty,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        elif x==3:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select pid from product where pid='{}'".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Price=input("\t\t  Enter New Price\t\t:")
                    sql="update product set Price={} where pid='{}'".format(Price,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        elif x==4:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select pid from product where pid='{}'".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Category=input("\t\t  Enter New Company Name\t\t:")
                    sql="update product set companyname='{}' where pid='{}''".format(Category,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        elif x==5:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select pid from product where pid='{}'".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Category=input("\t\t  Enter New Dom\t\t:")
                    sql="update product set dom='{}' where pid='{}'".format(Category,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        elif x==6:
            Ide=input("\t\t  Enter Id To Be Modified\t:")
            if Ide.isdigit():
                query="select pid from product where pid='{}'".format(Ide)
                cur.execute(query)
                rec=cur.fetchall()
                if rec!=[]:
                    Category=input("\t\t  Enter New Doe\t\t:")
                    sql="update product set doe='{}' where pid='{}'".format(Category,Ide)
                    cur.execute(sql)
                    cur.execute("commit")
                    print("")
                    print("\t\t\t","-"*30,sep="")
                    print("\t\t\t|Record Modified SuccessFully|")
                    print("\t\t\t","-"*30,sep="")
                else:
                    print("\t\t\tId Does Not Exist")
            else:
                print("Invalid Id, should be an integer")
        else:

            break
            


def stodisplay():
    sql="select * from product"
    cur.execute(sql)
    rec=cur.fetchall()
    query="select catid,catname from category"
    cur.execute(query)
    recnew=cur.fetchall()
    ltemp=[]
    dtemp={}
    l=[]
    for i in rec:
        ltemp.append(i[1])
    for i in recnew:
        dtemp[i[0]]=i[1]
    for i in rec:
        l.append(dtemp[i[1]])
    print("\tRecords : ")
    print("\n\t+------------+--------------------+------------------------------+---------+-------------+------------------+------------+------------+")
    print("\t| Product_ID |    Product_Name    |          Category_Name       |   qty   |     price   |    Company Name  |     dom    |    doe     |")
    print("\t+------------+--------------------+------------------------------+---------+-------------+------------------+------------+------------+")
    count=0
    for i in rec:
        print('\t| {}|{}|{}|{}|{}|{}|{}|{}|'.format(str(i[0]).rjust(11),str(i[2]).rjust(20),str(l[count]).rjust(30),str(i[3]).rjust(9),str(i[4]).rjust(13),str(i[5]).rjust(18),str(i[7]).rjust(12),str(i[8]).rjust(12)))
        print("\t+------------+--------------------+------------------------------+---------+-------------+------------------+------------+------------+")
        count+=1

def deletep():
    print("")
    print("\t\t\t","-"*4,"Deleting Product","-"*4)
    print("\t\t","_"*41)
    try:
        Id=input("\t\t  Enter Product Id To Be Deleted:")
        if Id.isdigit():
            sql="delete from Product where pid={}".format(Id)
            cur.execute(sql)
            cur.execute("commit")
            print("")
            print("\t\t\t","-"*29,sep="")
            print("\t\t\t|Record Deleted SuccessFully|")
            print("\t\t\t","-"*29,sep="")
        else:
            print("\t\t\tInvalid Id, should be a integer")
    except:
        print("\t\t\tProduct Id does not exist, Try Again")
        deletep()


def deletec():
    print("")
    print("\t\t\t","-"*4,"Deleting Category","-"*4)
    print("\t\t","_"*41)
    try:
        Id=input("\t\t  Enter Category Id To Be Deleted:")
        if Id.isdigit():
            sql="delete from category where catid={}".format(Id)
            cur.execute(sql)
            cur.execute("commit")
            print("")
            print("\t\t\t","-"*29,sep="")
            print("\t\t\t|Record Deleted SuccessFully|")
            print("\t\t\t","-"*29,sep="")
        else:
            print("\t\t\tInvalid Id, should be a integer")
    except:
        print("\t\t\tCategory Id does not exist, Try Again")
        deletec()

def stograph():
    import matplotlib.pyplot as plt
    sql="select qty from product;"
    cur.execute(sql)
    rec=cur.fetchall()
    query="select pname from product;"
    cur.execute(query)
    rec1=cur.fetchall()
    l1=[]
    l2=[]
    for i in rec:
        for j in i:
             l1.append(int(j))
    for i in rec1:
        for j in i:
             l2.append(j)
    plt.title("ITEM STOCKS")
    plt.xlabel("ITEM")
    plt.ylabel("STOCKS")
    plt.bar(l2,l1,color=["crimson","aqua","deepskyblue","tomato"],align="center",width=0.3)
    plt.xticks(rotation="vertical")
    plt.show()

# def sale():
#     import matplotlib.pyplot as plt
#     conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="group62")
#     cur=conn.cursor() 
#     print("\t\t","_"*41)
#     d=input("\t\t  Enter Sales Date\t\t:")
#     sql="select sales, product  from sale where sale_date='{}' group by product_name".format(d)
#     cur.execute(sql)
#     rec=cur.fetchall()
#     l1=[]
#     l2=[]
#     for i in rec:
#         l2.append(i[0])
#         l1.append(i[1])
#     plt.title("DAILY SALES REPORT-"+str(d))
#     plt.xlabel("ITEM")
#     plt.ylabel("SALES")
#     plt.bar(l1,l2,color=["crimson","aqua","deepskyblue","tomato"],align="center",width=0.1)
#     plt.show()

# def category_sale():
#     import matplotlib.pyplot as plt
#     conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="group62")
#     cur=conn.cursor() 
#     print("\t\t","_"*41)
#     sql="""SELECT c.catname, DATE_FORMAT(o.dop, '%m') AS month, SUM(p.price * ca.qty)"revenue"
# FROM category c
# INNER JOIN product p ON c.catid = p.catid
# INNER JOIN orderprod op ON p.pid = op.pid
# INNER JOIN payment o ON op.orderid = o.orderid
# INNER JOIN cart ca ON ca.cid=o.cid
# GROUP BY c.catname, DATE_FORMAT(o.dop, '%m') with rollup;"
#     SELECT c.catname, DATE_FORMAT(o.dop, '%m') AS month, SUM(p.price * ca.qty)"revenue"""
#     cur.execute(sql)
#     rec=cur.fetchall()
#     l1=[]
#     l2=[]
#     for i in rec:
#         if i[1]!=None and i[2]!=0:
#             l1.append(i[0])
#             l2.append(i[2])
#     plt.title("Revenue Across Category")
#     plt.xlabel("Category")
#     plt.ylabel("Revenue")
#     plt.bar(l1,l2)
#     plt.xticks(rotation="vertical")
#     plt.show()
# # category_sale()

def sale():
    import matplotlib.pyplot as plt 
    print("\t\t","_"*41)
    sql="""SELECT DATE_FORMAT(dop, '%m') AS month, SUM(totamount) AS revenue
FROM orders
JOIN payment ON orders.orderid = payment.orderid
GROUP BY month
ORDER BY month ASC;"""
    cur.execute(sql)
    rec=cur.fetchall()
    l1=[]
    l2=[]
    for i in rec:
        l1.append(i[0])
        l2.append(i[1])
    plt.title("Revenue Across Month")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.bar(l1,l2)
    # plt.xticks(rotation="vertical")
    plt.show()

def giveawaydeals():
    while True:
        amount=input("\t\t  Enter the amount(discount will be applied on order above this amount):")
        discount=input("\t\t  Enter the discount\t\t\t\t\t\t\t  :")
        try:
            sql="insert into deals values ({},{})".format(amount,discount)
            cur.execute(sql)
            cur.execute("commit")
            print("\t\t\t-----------------------")
            print("\t\t\tDeal Added Successfully")
            print("\t\t\t-----------------------")
            ans=input("\t\t  Do you want to continue(y/n)\t\t\t\t : ")
            if ans.lower()=="y":
                continue
            elif ans.lower()=="n":
                break
            else:
                print("\t\tInvalid choice,Try again")
        except:
            print("\t\t\tDeal for this amount already exist, Try Again!")

"""Admin portal done"""##########


"""Customer Portal"""###########


def addtocart(pid,cid):
    print("\n")
    print("\t\t","_"*48)
    print(''' 
\t\t\t\t█▀▀  ▄▀█  █▀█  ▀█▀
\t\t\t\t█▄▄  █▀█  █▀▄   █ ''')
    print("\t\t","_"*48)
    qty=int(input("\n\t\t\tEnter the qty you want:"))
    query="select qty from product where pid = {}".format(pid)
    cur.execute(query)
    rec=cur.fetchall()
    try:
        if int(rec[0][0])>=qty:
            cur.execute("select max(cartid) from cart")
            recid=cur.fetchall()
            sql="insert into cart values ({},{},{},{})".format(pid,qty,str(recid[0][0]+1),cid)
            cur.execute(sql)
            cur.execute("commit")
            print("\t\t\t----------------------------")
            print("\t\t\t|Added to Cart Successfully|")
            print("\t\t\t----------------------------")
        else:
            print("\t\t\t\tQty Insufficient")
            print("\n")
    except:
        print("\t\t\tCart id already exist, Try Again!")
        print("\n")
    return
    
def menu(cid):
    sql="select * from category"
    cur.execute(sql)
    rec=cur.fetchall()
    print("\t\t\t\t 𝕻𝖗𝖔𝖉𝖚𝖈𝖙 𝕮𝖆𝖙𝖆𝖑𝖔𝖌𝖚𝖊")
    print("\t+-----------+-----------------------------------+---------------------------------------------+")
    print("\t|   Choice  |         Category_Name             |          Description                        |")
    print("\t+-----------+-----------------------------------+---------------------------------------------+")
    count=1
    for i in rec:
        print('\t| {}|{}|{}|'.format(str(count).rjust(10),str(i[1]).rjust(35),str(i[2]).rjust(45)))
        print("\t+----------+------------------------------------+---------------------------------------------+")
        count+=1
    ch=0
    while True:
        print("\t\t","*"*70)
        choice=int(input("\t\t\tEnter Your Choice Of Category to See Related Products\t:"))
        print("\t\t",'*'*70)
        res=rec[choice-1]
        # print(res)
        sql="select * from product where catid='{}'".format(res[0])
        cur.execute(sql)
        rec1=cur.fetchall()
        print("\t+------------+-------------------------+---------------+-------------------------+--------------------------------+")
        print("\t| Product_Id |     Product_Name        |     price     |      Company Name       |          Description           |")
        print("\t+------------+-------------------------+---------------+-------------------------+--------------------------------+")
        for i in rec1:
            print('\t| {}|{}|{}|{}|{}|'.format(str(i[0]).rjust(11),str(i[2]).rjust(25),str(i[4]).rjust(15),str(i[5]).rjust(25),str(i[6]).rjust(32)))
            print("\t+------------+-------------------------+---------------+-------------------------+--------------------------------+")
        count+=1
        review=input("\t\tDo you also want to see review of the product(y/n) : ")
        if review.lower()=="y":
            rpid=input("\t\tEnter product id for the review of product you want to see:")
            qurev="select review from review where pid={}".format(rpid)
            cur.execute(qurev)
            reco1=cur.fetchall()
            quname="select pname from product where pid={}".format(rpid)
            cur.execute(quname)
            reco2=cur.fetchall()
            # print("\n\t\t\t\t----------------------------------")
            # print("\t\t\t\t Product Name   |    Description")
            # print("\t\t\t\t----------------------------------")
            # print("\t\t\t\t  ",reco2[0][0],"\t|\t",reco1[0][0])
            # print("\t\t\t\t----------------------------------")
            viewreview(rpid)
        print("\t\tAdd to Cart - (For Cart(C))")
        print("\t\tView More   - (For More(M)) ")
        print("\t\tGo Back     - (For Back(B)) ")
        y=input("\n\t\tYour choice? : ")
        if y.lower()=="m":
            continue
        elif y.lower()=="c":
            print("\n")
            print("\t\t--------------------------------------------------------------")
            prodid=input("\t\tEnter product id for the product that you want to add to cart:")
            print("\t\t--------------------------------------------------------------")
            addtocart(prodid,cid)
            return
        else:
            return

def showavailaibledeals():
    sql="select * from deals;"
    cur.execute(sql)
    rec=cur.fetchall()
    print("\n\t\tDeals : ")
    print("\t\t+---------------------+---------------+")
    print("\t\t| Orders Above Amount |    Discount   |")      
    print("\t\t+---------------------+---------------+")
    for i in rec:
        print('\t\t| {}|{}|'.format(str(i[0]).rjust(20),str(i[1]).rjust(15)))
        print("\t\t+---------------------+---------------+")
    return

def viewmembership(cid):
    sql="select membership from customer where cid = {}".format(cid)
    cur.execute(sql)
    rec=cur.fetchall()
    if rec[0][0]=='yes':
        print("\t\t\tYou are a member")
    else:
        print("\t\t\tYou are currently not a member")


def viewcart(cid):
    query="select * from cart where cid={}".format(cid)
    cur.execute(query)
    rec=cur.fetchall()
    print("\n\t\tCart : ")
    print("\t\t+----------+---------------------+---------------+")
    print("\t\t|  Cart Id |     Product Name    |    Quantity   |")      
    print("\t\t+----------+---------------------+---------------+")
    for i in rec:
        sql="select pname from product where pid={}".format(i[0])
        cur.execute(sql)
        recnew=cur.fetchall()
        print('\t\t| {}|{}|{}|'.format(str(i[2]).rjust(9),str(recnew[0][0]).rjust(21),str(i[1]).rjust(15)))
        print("\t\t+----------+---------------------+---------------+")
    return

def emptycart(cid):
    try:
        id=input("\t\t\tEnter cartid for the product you want to delete :")
        sql="delete from cart where cid={}".format(cid)
        cur.execute(sql)
        cur.execute("commit")
        print("\t\t\t----------------------------")
        print("\t\t\t|Record Deleted Succesfully|")
        print("\t\t\t----------------------------")
    except:
        print("\t\t\tId does not exist,Try Again")

def viewreview(pid):
    qurev="select review,cid from review where pid={}".format(pid)
    cur.execute(qurev)
    reco1=cur.fetchall()
    quname="select pname from product where pid={}".format(pid)
    cur.execute(quname)
    reco2=cur.fetchall()
    print("\n\t\tReview : ")
    print("\t\t\t+---------------------+------------------+---------------------+")
    print("\t\t\t|    Product Name     |     Review       |     User Name       |")
    print("\t\t\t+---------------------+------------------+---------------------+")
    for i in reco1:
        sql="select cname from customer where cid={}".format(i[1])
        cur.execute(sql)
        recsql=cur.fetchall()
        print('\t\t\t| {}|{}|{}|'.format(str(reco2[0][0]).rjust(20),str(i[0]).rjust(18),str(recsql[0][0]).rjust(21)))
        print("\t\t\t+---------------------+------------------+---------------------+")
    return

def trackorder(cid):
    sql="select orderid,empid from orders where cid={}".format(cid)
    cur.execute(sql)
    rec=cur.fetchall()
    d=dict()
    if rec!=[]:
        for i in rec:
            cur.execute("select empname from delivery_person where empid={}".format(i[1]))
            empnamerec=cur.fetchall()
            cur.execute("select paystatus,dod from delivery_details where orderid={}".format(i[0]))
            rec=cur.fetchall()
            d[i[0]]=tuple([empnamerec[0][0],rec[0][0],rec[0][1]])
            
        print("\n\t\tTrack Order : ")
        print("\t\t\t+---------------+---------------------+-------------------+-------------------+")
        print("\t\t\t|    orderid    |    Employee Name    |    Pay Status     |  Date of Delivery |")
        print("\t\t\t+---------------+---------------------+-------------------+-------------------+")
        for i in d:
            print('\t\t\t| {}|{}|{}|{}|'.format(str(i).rjust(14),str(d[i][0]).rjust(21),str(d[i][1]).rjust(19),str(d[i][2]).rjust(19)))
            print("\t\t\t+---------------+---------------------+-------------------+-------------------+")
    else:
        print("\n\n\t\t\t---------------------------------------------")
        print("\t\t\t|You do not have any current order right now|")
        print("\t\t\t---------------------------------------------")
    # except:
    #     print("Id does not exist, Try Again")
    return


def checkout(cid):
    cur.execute("select cname from customer where cid={}".format(cid))
    name=cur.fetchall()
    sql="select * from cart where cid='{}'".format(cid)
    cur.execute(sql)
    rec=cur.fetchall()
    amount=0
    cur.execute("select empid,empname from delivery_person;")
    empid=cur.fetchall()
    unitprice=[]
    product=[]
    qty=[]
    tamount=[]
    get_index = random.randrange(len(empid))
    # empname=empid[get_index][1]
    for i in rec:
        query="select pname,price from product where pid={}".format(i[0])
        cur.execute(query)
        pricerec=cur.fetchall()
        product.append(pricerec[0][0])
        unitprice.append(pricerec[0][1])
        qty.append(i[1])
        amount+=pricerec[0][1]*i[1]
        tamount.append(amount)
        sql="insert into orders values ({},{},{},{},{})".format("NULL",i[2],cid,empid[get_index][0],amount)
        cur.execute(sql)
        cur.execute("commit")
        today = date.today()
        cur.execute("select max(orderid) from orders;")
        orid=cur.fetchall()
        query="insert into delivery_details values ({},'{}',{},'{}','{}')".format(empid[get_index][0],today,orid[0][0],"NO","YES")
        cur.execute(query)
        cur.execute("commit")
    # cur.execute("delete from cart where cid={}".format(cid))
    # cur.execute("commit")
    print("""\t\t    _______   ______  __        __       
                  |       \ |      \|  \      |  \      
                  | $$$$$$$\ \$$$$$$| $$      | $$      
                  | $$__/ $$  | $$  | $$      | $$      
                  | $$    $$  | $$  | $$      | $$      
                  | $$$$$$$\  | $$  | $$      | $$      
                  | $$__/ $$ _| $$_ | $$_____ | $$_____ 
                  | $$    $$|   $$ \| $$     \| $$     \ 
                    $$$$$$$  \$$$$$$ \$$$$$$$$ \$$$$$$$$ """)
    
    print("\n\t   +--------------------+------------+----------+----------------+")
    print("\t   |  Product_Name      | Unit Price | Quantity |       Price    |")
    print("\t   +--------------------+------------+----------+----------------+")
    for i in range(len(unitprice)):
        print('\t   | {}   |{}|{}|{}|'.format(product[i].ljust(16),str(unitprice[i]).rjust(12),str(qty[i]).rjust(10),str(tamount[i]).rjust(16)))
        print("\t   +--------------------+------------+----------+----------------+")
    print()
    tax=0.1*sum(tamount)
    am=sum(tamount)+tax
    cur.execute("select * from deals;")
    rec=cur.fetchall()
    high=0
    for i in rec:
        if i[0]>i[high] and i[0]<am:
            high=i
    discount=rec[high][1]
    print("\n\t   Customer Name\t\t :",name[0][0])
    print("\t   Total Amount\t\t\t :",sum(tamount))
    print("\t   Delivery Charge(@10%)\t :",tax)
    print("\t   Amount after delivery charge\t :",am)
    print("\n\t   Since your total amount is greater than",rec[high][0],"you are eligible for",discount,"'%' discount")
    print("\n\t   Final Amount To Be Paid\t :",am-(am*discount/100))
    print("\n")
    print("\t\t\t+--------------------------+")
    print("\t\t\t|Thank You,Repay your Visit|")
    print("\t\t\t+--------------------------+")
    print("\t  "," ______"*10)
    print("\t  ","/_____/"*10)
    return

def returnproduct(cid):
    cur.execute("select orderid,cid from orders where cid={}".format(cid))
    rec=cur.fetchall()
    print("\t\t\t--------------------------")
    print("\t\t\t  Orderid    |    cid")
    print("\t\t\t--------------------------")
    for i in rec:
        print("\t\t\t  ",i[0],"\t     |\t",i[1])
    print("\t\t\t--------------------------")
    id=input("\t\t\tEnter orderid that you want to return : ")
    cur.execute("select empid from delivery_details where orderid={}".format(id))
    recid=cur.fetchall()
    cur.execute("insert into returnsp value ({},{},{},'{}','{}','{}')".format(id,recid[0][0],"NULL","NO","NO","NO"))
    cur.execute("commit")
    print("\n\t\t\t  ---------------------------------")
    print("\t\t\t     Return Inititated Sucessfully")
    print("\t\t\t  ---------------------------------")
    return
"""Customer Portal Done"""###########

def adminlogin(window):
    conn = mysql.connector.connect(
        host="localhost", user="root", passwd="root", database="group62")
    cur = conn.cursor()
    from tkinter import messagebox
    window.destroy()
    window1 = Tk()
    window1.geometry("750x530")
    window1.resizable(width=False, height=False)
    photo = PhotoImage(file='C:\\Users\\tusha\\Downloads\\adbgimage.png')
    l = Label(window1, image=photo)
    l.pack()
    image = PhotoImage(file='C:\\Users\\tusha\\Downloads\\adminp.png')
    l1 = Label(window1, image=image)
    l1.place(x=280, y=90)
    l2 = Label(window1, text="ADMIN LOGIN", font=(
        "Lucida handwriting", 18, "bold"), bg="black", fg="sky blue")
    l2.place(x=230, y=10, height=70, width=250)
    l3 = Label(window1, text="ENTER ADMINID     :", font=(
        "Lucida", 20, "bold"), bg="black", fg="khaki")
    l3.place(x=100, y=250)
    l4 = Label(window1, text="ENTER PASSWORD:", font=(
        "Lucida", 20, "bold"), bg="black", fg="khaki")
    l4.place(x=100, y=340)
    us = StringVar()
    ps = StringVar()
    x = Entry(window1, textvariable=us, font=(
        "Lucida", 16, "bold"), borderwidth=5)
    x.place(x=450, y=250)
    y = Entry(window1, textvariable=ps, font=(
        "Lucida", 16, "bold"), show="*", borderwidth=5)
    y.place(x=450, y=340)

    def show():
        hidebutton = Button(window1, image=hideimage,
                            command=hide, borderwidth=5)
        hidebutton.place(x=670, y=343)
        y.config(show="")

    def hide():
        showbutton = Button(window1, image=showimage,
                            command=show, borderwidth=5)
        showbutton.place(x=670, y=343)
        y.config(show="*")
    showimage = PhotoImage(file='C:\\Users\\tusha\\Downloads\\showimage.png')
    hideimage = PhotoImage(file='C:\\Users\\tusha\\Downloads\\hideimage.png')
    showbutton = Button(window1, image=showimage, command=show, borderwidth=5)
    showbutton.place(x=670, y=343)

    def myfun():
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="root", database="group62")
        cur = conn.cursor()
        usid = us.get()
        pas = ps.get()
        query = "select aid from admin where aid ='{}'".format(usid)
        cur.execute(query)
        reco = cur.fetchall()
        if reco != []:
            sql = "select apassword from admin where aid='{}'".format(usid)
            cur.execute(sql)
            rec = cur.fetchall()
            if rec[0][0] == pas:
                messagebox.showinfo("Admin Message", "Sign in Successfully")
                window1.destroy()
                while True:
                        print("\t\t", "_"*41)
                        print("\t\t", "^"*8, "\tAdmin Portal\t", "^"*9)
                        print("\t\t", "_"*41)
                        print("\t\t\tChoice\t\t|\tAction")
                        print("\t\t", "_"*41)
                        print("\t\t\t1.\t\t|\tAdd")
                        print("\t\t\t2.\t\t|\tModify")
                        print("\t\t\t3.\t\t|\tDisplay")
                        print("\t\t\t4.\t\t|\tDelete")
                        print("\t\t\t5.\t\t|\tSet Give Away Deals")
                        print("\t\t\t6.\t\t|\tAnalysis")
                        print("\t\t\t7.\t\t|\tExit")
                        print("\t\t", "_"*41)
                        choice = int(input("\t\t\tEnter Your Choice\t:"))
                        if choice == 1:
                            ques = input("\t\t\tDo you want to add product or category(p/c):")
                            print("\t\t", "_"*41)
                            if ques.lower() == 'p':
                                 Addp()
                            elif ques.lower() == 'c':
                                 Addc()
                            else:
                                 print("\t\t\tInvalid choice, Try again!")
                        elif choice == 2:
                            ques = input("\t\t\tDo you want to modify product or category(p/c):")
                            print("\t\t", "_"*41)
                            if ques == 'p':
                                 modifyp()
                            elif ques == 'c':
                                 modifyc()
                            else:
                                 print("\t\t\tInvalid choice, Try again!")
                        elif choice==3:
                            print("\t\t","_"*41)
                            stodisplay()
                        elif choice==4:
                            ques = input("\t\t\tDo you want to delete product or category(p/c):")
                            print("\t\t", "_"*41)
                            if ques == 'p':
                                 deletep()
                            elif ques == 'c':
                                 deletec()
                            else:
                                 print("\t\t\tInvalid choice, Try again!")
                        elif choice==5:
                            giveawaydeals()
                        elif choice==6:
                            while True:
                                print("\t\t","_"*41)
                                print("\t\t\tChoice\t\t|\tAction")
                                print("\t\t","_"*41)
                                print("\t\t\t1.\t\t|\tStockVsItem")
                                print("\t\t\t2.\t\t|\tMonthly Revenue")
                                print("\t\t\t3.\t\t|\tExit")
                                print("\t\t","_"*41)
                                Choice=int(input("\t\t\tEnter Your Choice\t:"))
                                if Choice==1:
                                    stograph()
                                elif Choice==2:
                                    sale()
                                else:
                                    break
                        elif choice==7:
                            window2=Tk()
                            mainmenu(window2)
                            break
                        else:
                            print("\t\t","_"*41)
                            print("\t\t  Invalid Entry")
                            print("")
                            ans=input("\t\t  Do You Want To Cont.(y/n):")
                            if ans=="y" or ans=="Y":
                                continue
                            else:
                                break


            else:
                messagebox.showerror("Error","Incorrect Password,Try Again")
        else:
            messagebox.showerror("Error","User Does Not Exist")
    Button(text="Log In",command=myfun,bg="black",font=("elephant",20),fg="khaki").place(x=160,y=420,height=80,width=180)
    Button(text="BACK <--",command=lambda:mainmenu(window1),bg="black",font=("elephant",20),fg="khaki").place(x=400,y=420,height=80,width=180)
    window1.mainloop()




def signup(window):
    window.destroy()
    conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="group62")
    cur=conn.cursor()
    from tkinter import messagebox
    window1=Tk()
    window1.resizable(width=False,height=False)
    image=PhotoImage(file='C:\\Users\\tusha\\Downloads\\custsignimage.png')
    l1=Label(window1,image=image)
    l1.pack()
    l2=Label(window1,text="Customer Signup",font=("lucida ",20,"bold"),bg="black",fg="linen")
    l2.place(x=200,y=5,height=70,width=300)
    l3=Label(window1,text="ENTER YOUR NAME :",font=("Lucida",20,"bold"),bg="black",fg="linen")
    l3.place(x=50,y=100)
    l4=Label(window1,text="ENTER PHONE NO    :",font=("lucida",20,"bold"),bg="black",fg="linen")
    l4.place(x=50,y=150)
    l5=Label(window1,text="ENTER USER-ID       :",font=("lucida",20,"bold"),bg="black",fg="linen")
    l5.place(x=50,y=200)
    l8=Label(window1,text="ENTER PASSWORD :",font=("Lucida",20,"bold"),bg="black",fg="linen")
    l8.place(x=50,y=250) 
    l7=Label(window1,text="Sex(M/F)                :",font=("Lucida",20,"bold"),bg="black",fg="linen")
    l7.place(x=50,y=300)
    l6=Label(window1,text="ENTER DOB(yy-mm-dd):",font=("lucida",20,"bold"),bg="black",fg="linen")
    l6.place(x=50,y=350)
    name=StringVar()
    ph=StringVar()
    uid=StringVar()
    upswd=StringVar()
    usex=StringVar()
    udb=StringVar()
    try:
        x1=Entry(window1,textvariable=name,font=("Lucida",18,"bold"),borderwidth=5)
        x1.place(x=450,y=100)
        x2=Entry(window1,textvariable=ph,font=("Lucida",18,"bold"),borderwidth=5)
        x2.place(x=450,y=150)
        x3=Entry(window1,textvariable=uid,font=("Lucida",18,"bold"),borderwidth=5)
        x3.place(x=450,y=200)
        x4=Entry(window1,textvariable=upswd,font=("Lucida",18,"bold"),borderwidth=5)
        x4.place(x=450,y=250)
        x5=Entry(window1,textvariable=usex,font=("Lucida",18,"bold"),borderwidth=5)
        x5.place(x=450,y=300)
        x6=Entry(window1,textvariable=udb,font=("Lucida",18,"bold"),borderwidth=5)
        x6.place(x=450,y=350)
        def myfun():
            conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="group62")
            cur=conn.cursor()
            cur.execute("select * from customer where cid={}".format(uid.get()))
            rec=cur.fetchall()
            if rec==[]:
                sql="insert into customer values ('{}','{}','{}','{}','{}','{}','{}')".format(uid.get(),upswd.get(),name.get(),udb.get(),usex.get(),"no",ph.get())
                cur.execute(sql)
                cur.execute("commit")
                messagebox.showinfo("Admin Message","Sign up Successfully")
                user(window1)
            else:
                messagebox.showerror("Error", "Category Id Already Exist")
        Button(text="Sign up",command=myfun,bg="black",fg="linen",font=("lucida",22)).place(x=160,y=430)
        Button(text="BACK <--",command=lambda:user(window1),bg="black",fg="linen",font=("lucida",22)).place(x=450,y=430)
        window1.mainloop()
        
    except:
        messagebox.showerror("Error","Wrong Date Format,Try Again!")
        print("\t\t\t-----------------------------")
        print("\t\t\tWrong Date Format , Try Again")
        print("\t\t\t-----------------------------")


def custologin(window2):
    conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="group62")
    cur=conn.cursor()
    from tkinter import messagebox
    window2.destroy()
    window=Tk()
    window.resizable(width=False,height=False)
    hoto=PhotoImage(file='C:\\Users\\tusha\\Downloads\\custloginbg.png')
    l1=Label(window,image=hoto)
    l1.pack()
    image=PhotoImage(file='C:\\Users\\tusha\\Downloads\\custlogin.png')
    l1=Label(window,image=image)
    l1.place(x=310,y=90)
    l2=Label(window,text="USER LOGIN",font=("Lucida",20,"bold"),bg="darkorange4",fg="snow")
    l2.place(x=240,y=10,height=70,width=300)
    l3=Label(window,text="ENTER USERID       :",font=("Lucida",20,"bold"),bg="black",fg="khaki1")
    l3.place(x=110,y=280)
    l4=Label(window,text="ENTER PASSWORD:",font=("Lucida",20,"bold"),bg="black",fg="khaki1")
    l4.place(x=110,y=330)
    us=StringVar()
    ps=StringVar()
    x=Entry(window,textvariable=us,borderwidth=5,font=("Lucida",18,"bold"))
    x.place(x=420,y=280)
    y=Entry(window,textvariable=ps,show="*",borderwidth=5,font=("Lucida",18,"bold"))
    y.place(x=420,y=330)
    def show():
        hidebutton = Button(window, image=hideimage,
                            command=hide, borderwidth=5)
        hidebutton.place(x=660, y=335)
        y.config(show="")

    def hide():
        showbutton = Button(window, image=showimage,
                            command=show, borderwidth=5)
        showbutton.place(x=660, y=335)
        y.config(show="*")
    showimage = PhotoImage(file='C:\\Users\\tusha\\Downloads\\showimage.png')
    hideimage = PhotoImage(file='C:\\Users\\tusha\\Downloads\\hideimage.png')
    showbutton = Button(window, image=showimage, command=show, borderwidth=5)
    showbutton.place(x=660, y=335)
    def myfun():
        conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="group62")
        cur=conn.cursor()
        usid=us.get()
        pas=ps.get()
        cur.execute("delete from cart where cid={}".format(usid))
        cur.execute("commit")
        query="select cid from customer where cid ={}".format(usid)
        cur.execute(query)
        reco=cur.fetchall()
        if reco!=[]:
            sql="select cpassword from customer where cid='{}'".format(usid)
            cur.execute(sql)
            rec=cur.fetchall()
            if rec[0][0]==pas:
                messagebox.showinfo("Admin Message","Logged In Successfully")
                window.destroy()
                while True:
                    print("\t\t","_"*41)
                    print("\t\t","^"*9,"\tShopZen\t","^"*9)
                    print("\t\t","_"*41)
                    print("\t\t\tChoice\t\t|\tAction")
                    print("\t\t\t1.  \t\t|\tExlore Product Catalogue")
                    print("\t\t\t2.  \t\t|\tShow Available Deals")
                    print("\t\t\t3.  \t\t|\tAdd Product to Cart")
                    print("\t\t\t4.  \t\t|\tView Membership Status")
                    print("\t\t\t5.  \t\t|\tView Cart")
                    print("\t\t\t6.  \t\t|\tEmpty Cart")
                    print("\t\t\t7.  \t\t|\tView Review")
                    print("\t\t\t8.  \t\t|\tExit Cart/Check Out")
                    print("\t\t\t9.  \t\t|\tTrack your order")
                    print("\t\t\t10. \t\t|\tReturn a product")
                    print("\t\t\t>10.\t\t|\tExit")
                    print("\t\t","_"*41)
                    choice=int(input("\t\t\tEnter Your Choice\t:"))
                    print("\t\t","_"*41)
                    if choice==1:
                        menu(usid)
                    elif choice==2:
                        showavailaibledeals()
                    elif choice==3:
                        prodid=input("\t\t\tEnter product id for the product that you want to add to cart:")
                        addtocart(prodid,usid)
                    elif choice==4:
                        viewmembership(usid)
                    elif choice==5:
                        viewcart(usid)
                    elif choice==6:
                        emptycart(usid)
                    elif choice==7:
                        prodid=input("\t\t\tEnter product id for the product that you want to add to cart:")
                        viewreview(prodid)
                    elif choice==8:
                        checkout(usid)
                    elif choice==9:
                        trackorder(usid)
                    elif choice==10:
                        returnproduct(usid)
                    else:
                        window1=Tk()
                        mainmenu(window1)
                        break

            else:
                messagebox.showerror("Error","Incorrect Password,Try Again")
        else:
            messagebox.showerror("Error","User Does Not Exist")
    Button(text="Log In",command=myfun,bg="black",fg="khaki",font=("elephant",22)).place(x=130,y=430)
    Button(text="BACK <--",command=lambda:user(window),bg="black",fg="khaki",font=("elephant",22)).place(x=450,y=430)
    window.mainloop()



def mainmenu(window):
    global hoto
    global photo
    global oto
    window.destroy()
    window1=Tk()
    window1.resizable(width=False,height=False)
    hoto=PhotoImage(file='C:\\Users\\tusha\\Downloads\\sebimage.png')
    Label(window1,image=hoto).pack()
    photo=PhotoImage(file='C:\\Users\\tusha\\Downloads\\adimage.png')
    Label(window1,image=photo).place(x=100,y=40)
    oto=PhotoImage(file='C:\\Users\\tusha\\Downloads\\usimage.png')
    Label(window1,image=oto).place(x=900,y=40)
    Button(text="ADMIN",command=lambda:adminlogin(window1),bg="black",fg="khaki",font=("lucida",26)).place(x=50,y=240,width=300,height=80)
    Button(text="USER",command=lambda:user(window1),font=("lucida",26),bg="black",fg="khaki").place(x=850,y=240,width=300,height=80)
    def myfun1():
        window1.destroy()
    Button(text="EXIT",command=myfun1,bg="black",fg="khaki",font=("lucida",26)).place(x=450,y=450,width=300,height=80)


def user(window):
     global photo
     window.destroy()
     window2=Tk()
     window2.geometry("800x510")
     window2.resizable(width=False,height=False)
     photo=PhotoImage(file='C:\\Users\\tusha\\Downloads\\usercolimage.png')
     Label(window2,image=photo).pack()
     l2=Label(window2,text="USER'S COLUMN",font=("Lucida Handwriting",26,"bold"),bg="black",fg="khaki")
     l2.place(x=210,y=10,height=70,width=400)
     a=StringVar()
     a.set("Login")
     Button(window2,text="Signup",command=lambda:signup(window2),bg="bisque2",font=("lucida",26,"bold")).place(x=30,y=170,width=300,height=100)
     Button(window2,text="Login",command=lambda:custologin(window2),bg="bisque2",font=("lucida",26,"bold")).place(x=485,y=170,width=300,height=100)
     Button(text="BACK <--",command=lambda:mainmenu(window2),bg="slate gray",font=("elephant",26)).place(x=250,y=400,width=300,height=100)
     window2.mainloop()



def supermainmenu():
    global photo,hoto
    window=Tk()
    window.geometry("840x500")
    # window.geometry("940x590")
    window.resizable(width=False,height=False)
    photo=PhotoImage(file='C:\\Users\\tusha\\Downloads\\inimage.png')
    Label(window,image=photo).pack()
    l2=Label(window,text="ShopZen",font=("Lucida Handwriting",24,"bold"),bg="Slateblue1",fg="white")
    l2.place(x=230,y=10,height=70,width=400)
    Button(text="CONTINUE",command=lambda:mainmenu(window),bg="Slateblue1",fg="white",font=("lucida handwriting",24)).place(x=280,y=415,height=70,width=300)
    window.mainloop()

supermainmenu()