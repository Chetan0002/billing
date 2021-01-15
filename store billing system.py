import json
a = open("C:/Users/Anushka T/Desktop/PYTHON PROJETCS/stock.txt",'r')
products = a.read() 
products = json.loads(products)
a.close()

option = 0
while option < 3:
    
    copy = 0
    
    bucket = {

    }

    print("\t\t\t\t\t\t\t\t=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t\t\t\t\t\t\t\t  STORE BILLING PROJECT")
    print("\t\t\t\t\t\t\t\t=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("--=======--")
    print("  OPTIONS")
    print("--=======--")
    print("1.Buy Products\n2.Update Stocks\n3.Exit")
    option = int(input("\nEnter Your Choice :- "))
    if option == 1:
        name = input("Enter Customer Name :- ")
        phone = input("Enter Customer Phone Number :- ")
        email = input("Enter Customer E-mail I.D :- ")
        make = 0
        while  make < 3 and make != 1:
            count = 0
            for i in products.keys():
                count = count + 1
                print(count,'.',i)
            buy = input("Enter Which Category You Want :- ")
            if buy in products.keys():
                h = 0
                for read in products[buy].keys():
                    h = h + 1
                    print(h,'.',read)
                get = input("Choose Which Item You Want :- ")
                qty = int(input("Enter Quantity Of Item You Want :- "))
                total = qty*products[buy][get]
                print("Total :- ",total)
                newbucket={
                        get:{
                        "Name":get,
                        "Quantity":qty,
                        "Total":total
                        }
                    }
                bucket.update(newbucket)
                print(bucket)
            print("\n-=-=-=-=-=-=-")
            print("More Options")
            print("-=-=-=-=-=-=-")
            print("1.Make Our Bill\n2.Buy More Products")
            make = int(input("\nChoose A Option :- "))
            if make == 1:
                print("\n=================================================")
                print("Thank You To Shop With Us Have A Great & Nice Day")
                print("=================================================")
                bill = open("C:/Users/Anushka T/Desktop/PYTHON PROJETCS/bills"+str(copy)+".txt",'w')
                bill.write("\t\t\t\t\t-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                bill.write("\n\t\t\t\t\tSTORE BILLLING PROJECT")
                bill.write("\n\t\t\t\t\t-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                bill.write("\n\n=======================================")
                bill.write("\nCustomer Name :- "+str(name))
                bill.write("\nCustomer Mobile Number :- "+str(phone))
                bill.write("\nCustomer E-Mail I.D :- "+str(email))
                bill.write("\n=======================================")
                bill.write("\nProduct Name\tQuantity\t\tTotal")
                bill.write("\n=======================================")
                
                for z in bucket: 
                    bill.write("\n"+bucket[z]["Name"]+"\t\t"+str(bucket[z]["Quantity"])+"\t\t"+str(bucket[z]["Total"]))
                nettotal = 0
                for j in bucket:
                    nettotal = nettotal+bucket[j]["Total"]
                netgst = nettotal*0.18
                grandtotal = nettotal+netgst
                
                bill.write("\n\n=======================================")
                bill.write("\nNetTotal : "+str(nettotal))
                bill.write("\nNetGst 18%  : "+str(netgst))
                bill.write("\nGrandTotal : "+str(grandtotal))
                bill.write("\n\n=======================================")
                bill.write("\n\nThank You To Shop With Us Have A Nice Day")
                bill.write("\n\n=======================================")
                bill.close()
    
    if option == 2:
        
        c = 0
        
        while c < 5:
            print("\n\n---============---")
            print("   MORE OPTIONS")
            print("---============---")
            print("1.Add New Category\n2.Add New Items To Category\n3.Delete Category\n4.Delete Items From Category\n5.Exit")
            c = int(input("\n\nEnter Your Choice :- "))
            if c == 1:
                for name in products.keys():
                    print(name)
                b = input("Enter New Category You Want :- ")
                newproducts = {
                    b:{

                    }
                }
                products.update(newproducts)
                print(products)
            if c == 2:
                for name in products.keys():
                    print(name)
                d = input("Enter Which Category You Want :- ")
                if d in products.keys():
                    newitems = input("Enter New Item Name You Want To Add :- ")
                    price = int(input("Enter Price Of New Item :- "))
                    newproducts={newitems:price}
                    products[d].update(newproducts)
                    print(products)
            if c == 3:
                for name in products.keys():
                    print(name)
                e = input("Enter Which Category You Want :- ")
                if e in products.keys():
                    products.pop(e)
                    print(products)
            if c == 4:
                for name in products.keys():
                    print(name)
                f = input("Enter Which Category You Want :- ")
                if f in products.keys():
                    for nname in products[f].keys():
                        print(nname)
                    g = input("Enter Which Items You Want :- ")
                    if g in products[f].keys():
                        products[f].pop(g)
                        print(products)

stocks = open("C:/Users/Anushka T/Desktop/PYTHON PROJETCS/stock"+str(copy)+".txt",'w')
p = json.dumps(products)
stocks.write(p)
stocks.close()