from kanren import *
from kanren.constraints import *
# medical diagnosys system.

symptoms = Relation()
diagnosis = Relation()
facts(symptoms, ("Flu", "Fever"),
                ("Cold", "Cough"),
                ("Flu", "Cough"),
                ("Cold", "Runnynose"),
                ("Flu", "Runnynose"),
                ("Cold", "Headache"))

facts(diagnosis, ("Flu", "Antibiotics"),
                 ("Cold", "Antihistamine"))

disease_v, symptoms_v, diagnosis_v = var(), var(), var()

# which disease can be cured by antibiotics?
print(set(run(0, disease_v, diagnosis(disease_v, symptoms_v), diagnosis(disease_v, "Antibiotics"))))

# which systoms can be cured by antihistamine?
print(set(run(0, symptoms_v, symptoms(disease_v, symptoms_v), diagnosis(disease_v, "Antihistamine"))))

# which diseases have a fever?
print(set(run(0, disease_v, symptoms(disease_v, symptoms_v), symptoms(disease_v, "Fever"))))