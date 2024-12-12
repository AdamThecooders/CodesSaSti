
while True:
    print("Hello I am Wealthy the chatbot of STI Doctors")
    print(".............................................")
    print("I can provide Information about services, Facilities, Visit hours, etc.")
    print(".............................................")
    print("KEY Chats: Hospital Overview | Facilities | Medical Services | Appointments | Visiting Hours")
    response1 = input("Enter your response: ").strip().lower()

    if response1 == "hospital overview":
        print("We are the Best Hospital in the world run by professional student graduates with 0 experience from STI ")
        back = input("Do you want to go back to the menu? (yes/no): ").strip().lower()
        if back != "yes":
            break

    elif response1 == "facilities":
        print("Our hospital offers state-of-the-art facilities for patient care and comfort.")
        back = input("Do you want to go back to the menu? (yes/no): ").strip().lower()
        if back != "yes":
            break

    elif response1 == "medical services":
        while True:
            facilities = input("""
1: Checkups | 2: X-ray | 3: Blood Test | 4: Emergency Services | 5: Surgeries
Enter the number for more info: """).strip()
            
            if facilities == "1":
                while True:
                    checkup = input("""
1. Pediatric, 2. General Health Checkup, 3. Dental Checkup
Enter the number for more info: """).strip()

                    if checkup == "1":
                        print("""
Pediatric: Check-up Children (0-18 years)
Purpose: To monitor growth, development, and early detection of health problems.
Common Tests/Exams:
- Growth measurements (weight, height, head circumference)
- Immunizations (vaccinations as per schedule)
- Hearing and vision screenings
- Developmental assessments (motor skills, language skills, cognitive milestones)
- Blood tests (if needed, e.g., for anemia, lead exposure)
- Physical exam (general health and wellness)
""")
                        continue
                    elif checkup == "2":
                        print("""
General Health Check-up (Full Body Check-up)
Purpose: To assess overall health, screen for common health conditions, and detect early signs of disease.
Common Tests/Exams:
- Blood pressure measurement
- Blood tests (lipid profile, glucose, kidney function, liver function)
- Chest X-ray (if necessary)
- Electrocardiogram (ECG) (if at risk for heart disease)
- BMI (Body Mass Index) check
""")
                        continue
                    elif checkup == "3":
                        print("""
Purpose: To monitor oral health and prevent dental problems like cavities and gum disease.
Common Tests/Exams:
- Teeth examination
- Fluoride treatments
- Cleanings and sealants
- X-rays (if needed)
""")
                        continue
                    else:
                        print("Invalid response. Please try again.")
                break
            elif facilities == "2":
                print("""
X-ray services:
We offer X-ray services for diagnostic purposes. Our X-ray machines are state-of-the-art and provide high-quality images.
Common uses:
- Diagnosing bone fractures
- Detecting lung diseases
- Monitoring the progression of diseases
""")
                break
            elif facilities == "3":
                print("""
Blood Test services:
We offer a wide range of blood tests to diagnose and monitor various health conditions.
Common tests:
- Complete Blood Count (CBC)
- Blood chemistry tests
- Lipid profile
- Liver function tests
""")
                break
            elif facilities == "4":
                print("""
Emergency Services:
Emergency Number: 0989312731231
We provide emergency services 24/7 for patients who require immediate medical attention.
Common emergencies:
- Cardiac arrest
- Stroke
- Severe injuries
- Severe allergic reactions
""")
                break
            elif facilities == "5":
                print("""
Surgeries:
We offer a range of surgical services, from minor procedures to complex operations.
Common surgeries:
- Appendectomy
- Cesarean section
- Hysterectomy
- Knee replacement
""")
                break
            else:
                print("Invalid response. Please try again.")

    elif response1 == "appointments":
        print("""
Appointments:
We offer appointments for various medical services, including check-ups, surgeries, and emergency services.
Types of appointments:
- New patient appointments
- Follow-up appointments
- Emergency appointments
- Surgery appointments
Contact us through:
- Email: STIdoctors@gmail.com
- Facebook Page: STIdoctors
- Hotline: 8431204
- Website: www.STIdoctors.com
""")
        back = input("Do you want to go back to the menu? (yes/no): ").strip().lower()
        if back != "yes":
            break

    elif response1 == "visiting hours":
        print("""
Department-Specific Visiting Hours:
- ICU: Limited visiting hours, please check with the ICU staff for specific times.
- Emergency Department: Open 24/7, but visiting hours may be restricted due to patient care and safety.
- Maternity: Visiting hours may vary depending on the patient's level of care and the hospital's policies.
- Pediatrics: Visiting hours may be restricted to immediate family members and caregivers.

Additional Information:
Please note that visiting hours may be subject to change due to hospital policies, patient care, and safety concerns.
It's always best to check with the hospital staff or the patient's nurse for the most up-to-date visiting hours and any specific restrictions.
""")
        back = input("Do you want to go back to the menu? (yes/end): ").strip().lower()
        if back == "end":
            print("Thank you for using Wealthy we hope to see you again")
            break
        elif back != "yes":
            print("Invalid response. Returning to menu.")

    else:
        print("Invalid response. Please try again.")
