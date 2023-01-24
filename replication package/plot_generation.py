import sys
import os, glob
import matplotlib.pyplot as plt
import subprocess

def mean(t):
    return (t[0] + t[1])/2

def getTS(fhandler):
    lsts = [list() for _ in [1, 2, 3]]
    for row in fhandler.readlines():
        temp = row.strip()
        if temp != '':
            temp = temp.replace('  ', ' ')
            temp = temp.split(' ')
            for i in range(0, len(temp)):
                y = temp[i]
                x = float(y)
                lsts[i].append(x)
    return tuple(lsts)


def visualize(dictionary):
    experiments = [
        (
            ('Consumed Energy','JAISE22_casestudy_energywinter.pdf'),
            'Time',
            ('energyfull_winter', 'Complete Model'),
            ('energypartial_winter', 'Partial Model')
        ),
        (
            ('Room1 Temperature','JAISE22_casestudy_temperaturewinter.pdf'),
            'Time',
            ('temperaturefull_winter', 'Complete Model'),
            ('temperaturepartial_winter', 'Partial Model')
        ),
        (
            ('Consumed Energy', 'JAISE22_casestudy_energysummer.pdf'),
            'Time',
            ('energyfull_summer', 'Complete Model'),
            ('energypartial_summer', 'Partial Model')
        ),
        (
            ('Room1 Temperature', 'JAISE22_casestudy_temperaturesummer.pdf'),
            'Time',
            ('temperaturefull_summer', 'Complete Model'),
            ('temperaturepartial_summer', 'Partial Model')
        ),
        (
            ('HVAC activation (%)', 'JAISE22_casestudy_activationsummer.pdf'),
            'Time',
            ('hvaccoolfull_summer', 'Complete Model'),
            ('hvaccoolpartial_summer', 'Partial Model')
        ),
        (
            ('Consumed Energy', 'JAISE22_casestudy_sensitivity.pdf'),
            'Time',
            ('energysensitivity_1', '#1 users'),
            ('energysensitivity_2', '#2 users'),
            ('energysensitivity_3', '#3 users'),
            ('energysensitivity_4', '#4 users')
        )
    ]
    for e in experiments:
        plotname, pdfname = e[0]
        time = dictionary[e[1]]
        for plots, linename in e[2:]:
            data = [(dictionary[plots]['max'][i], dictionary[plots]['min'][i]) for i in range(0, len(dictionary[plots]['min']))]
            line = list(map(mean,data))
            plt.plot(time, line, label=linename)
        plt.xlabel('time')
        plt.ylabel(plotname)
        plt.legend()
        plt.savefig(pdfname + ".pdf", format="pdf", bbox_inches="tight")
        plt.clf()

def execution():
    test = os.listdir('./')
    for item in test:
        if item.endswith(".out"):
            os.remove(os.path.join('./', item))
    #os.system('untitled.exe full.fspn')
    #os.system('untitled.exe partial.fspn')

if __name__ == '__main__':
    data = dict()
    isTimePresent = False
    for filename in glob.glob('./*.out'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            tagName = filename.split('\\')[-1].split('.')[0]
            timeTS, minTS, maxTS = getTS(f)
            if not isTimePresent:
                data['Time'] = timeTS
                isTimePresent = True
            data[tagName] = dict()
            data[tagName]['min'] = minTS
            data[tagName]['max'] = maxTS
    visualize(data)
    #execution()
