# Medical-Diagnosis-System

This is a simple medical diagnosis system implemented using the kanren library in Python. It uses a set of predefined symptoms and corresponding diagnoses to suggest potential diseases based on the symptoms entered by a user.

## Requirements
Python 3
kanren library

## How to Use
The system has two main functions, one that suggests potential diseases based on a given symptom and another that suggests symptoms based on a given diagnosis.

The symptoms and diagnosis relations are defined with the facts function, which accepts a list of tuples as its second argument. Each tuple represents a single symptom or diagnosis, with the first element being the name of the disease and the second element being the symptom or diagnosis.

The run function is used to query the system for potential diseases based on a given symptom or potential symptoms based on a given diagnosis. The first argument to run is the number of solutions to return (0 returns all solutions). The second argument is the variable to bind, with disease_v, symptoms_v, and diagnosis_v representing variables for the disease, symptoms, and diagnoses, respectively. The remaining arguments define the constraints to be satisfied.

## Conclusion
This is a basic implementation of a medical diagnosis system using the kanren library. The system can be extended by adding more symptoms and diagnoses to the symptoms and diagnosis relations, as well as modifying the constraints used in the run function to accommodate new data.



