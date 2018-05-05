from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
import requests
from django.http import HttpResponseRedirect



def index(request):
    if 'search' in request.GET:
        val = request.GET['search']
    else:
        return render(request, "pharmapedia/index.html")
    url = "https://pharmapedia.herokuapp.com/medicine?search=" + val;
    res = requests.get(url)
    obj = json.loads(res.content)
    result = []
    length = obj["header"][0];
    index = 0;
    for i in range(length):
        sets = {"index": str(index), "bname": obj["result"][i][0], "gname": obj["result"][i][1], "mode": obj["result"][i][2],
                "mft": obj["result"][i][3], "price": obj["result"][i][4], "infoset": obj["result"][i][5]}
        index = index+1;
        result.append(sets)
    print(result)
    return render(request, "pharmapedia/index2.html", context={"result": result})


"""   bname.append(obj["result"][i][0])
        gname.append(obj["result"][i][1])
        mode.append(obj["result"][i][2])
        mft.append(obj["result"][i][3])
        price.append(obj["result"][i][4])
        infoset.append(obj["result"][i][5])
        j.append(i)"""




def alternative(request):
    return render(request, "pharmapedia/drugs.html")



def dlocation(request):
    search=""
    if 'search' in request.GET and "loc" in request.GET :
        search = request.GET['search']
        loc= request.GET['loc']

        loc=loc.split(",")

        url = "https://pharmapedia.herokuapp.com/store#alpha?search="+search+"&lglt="+loc[0]+","+loc[1];
        res = requests.get(url)
        obj = json.loads(res.content)
        result = []
        length = obj["header"];
        index = 0;
        for i in range(length):
            sets = {"index": str(index), "name": obj["result"][i][0]["name"], "address": obj["result"][i][1]["add"],
                    "phone": obj["result"][i][2]["phone"], "email": obj["result"][i][3]["email"],
                    "distance": obj["result"][i][4]["distance"], "time": obj["result"][i][5]["time"],
                    "coordinate": obj["result"][i][6]["coord"]}
            index = index + 1
            result.append(sets)
        print(result)
        return render(request, "pharmapedia/Location.html", context={"search":search,"result": result})
    else:
        search = request.GET['search']
        return render(request, "pharmapedia/Location.html", context={"search":search,"result": []})



def index2(request):
    if 'search' in request.GET:
        val = request.GET['search']
    else:
        return render(request, "pharmapedia/index.html")
    url = "https://pharmapedia.herokuapp.com/medicine?search=" + val;
    res = requests.get(url)
    obj = json.loads(res.content)
    result = []
    length = obj["header"][0];
    index = 0;
    for i in range(length):
        sets = {"index": str(index), "bname": obj["result"][i][0], "gname": obj["result"][i][1],
                "mode": obj["result"][i][2], "mft": obj["result"][i][3], "price": obj["result"][i][4], "infoset": obj["result"][i][5]}
        index = index + 1;
        result.append(sets)
    print(result)
    return render(request, "pharmapedia/index2.html", context={"result": result})




def searchmft(request):

    if 'mft' in request.GET:
        mft = request.GET['mft']
        if mft!="all":
            url = "https://pharmapedia.herokuapp.com/manufacturer?mft=" + mft;
            res = requests.get(url)
            obj = json.loads(res.content)
            result = []
            length = obj["header"];
            index = 0;
            for i in range(length):
                sets = {"index": str(index), "bname": obj["data"][i]}
                index = index + 1;
                result.append(sets)
            return render(request, "pharmapedia/manufacturer.html", context={"mft":mft,"data": result})


    else:
        url = "https://pharmapedia.herokuapp.com/manufacturer?mft=all"
        res = requests.get(url)
        obj = json.loads(res.content)
        result = []
        length = obj["header"];
        s1 = "<h1> List of manufacturer"  "</h1>"
        s2 = ""
        for i in range(length):
            s2 = s2 + "<tr><td><a href='searchmft?mft=" + obj["data"][i] + "'>" + obj["data"][i] + "\n" + "</tr></td>"
        z = "<table><tr>" + s2 + "</tr></table>"
        return HttpResponse(s1 + "\n" + z, content_type = "text/html")




def bdrug(request):
    return render(request, "pharmapedia/bdrug.html")