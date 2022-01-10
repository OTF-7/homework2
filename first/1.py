school_subjects = ["Math", "Qura'an", "Physics", "IT", "chemistry", "biology"]
print("""
which of those subjects you don't like 
""")
print("\n".join(school_subjects))
awful_subject = input()
school_subjects.remove(awful_subject)
print("\n".join(school_subjects))