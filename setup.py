'''It is used by setup tools to define the configuration of your project, such as its metadata, dependencies,and more '''
from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    '''THIS FUnction will return list of requirements'''
    requirment_list:List[str]=[]
    try:
        with open('requirment.txt','r') as file:
            #read lines for the file 
            lines=file.readlines()
            #process each line 
            for line in lines:
                requirment=line.strip()
                ## ignore empty lines and -e.
                if requirment and requirment!='-e.':
                    requirment_list.append(requirment)
    except FileNotFoundError:
        print("requirment.txt file not found")

    return requirment_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Manas khatri",
    packages= find_packages(),
    install_requires=get_requirments()
)


                