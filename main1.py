
from pyscript import document

def compute_average(event):
    #Get the input value and convert to a float
    eng = float(document.getElementById("eng").value)
    math = float(document.getElementById("math").value)
    fil = float(document.getElementById("fil").value)
    sci = float(document.getElementById("sci").value)
    SS = float(document.getElementById("SS").value)
    PE = float(document.getElementById("PE").value)
    ICT = float(document.getElementById("ICT").value)
    mus = float(document.getElementById("mus").value)
    #Compute for average
    average = (eng + math + fil + sci + SS + PE + ICT + mus) / 8

    #Determine if pass or fail
    if average >=75:
        result = "Yes"
    else:
        result = "No"
    
    #Dispalying the result
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result