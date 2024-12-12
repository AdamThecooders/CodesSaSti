class HospitalChatbot:
    def __init__(self):
        # Store information about the hospital services in a dictionary
        self.services = {
            "overview": "We are a multi-specialty hospital providing quality healthcare services.",
            "facilities": {
                "emergency": "Our emergency department operates 24/7.",
                "outpatient": "We have outpatient clinics for cardiology, orthopedics, and more.",
                "inpatient": "We offer inpatient rooms with all necessary amenities for your comfort.",
                "surgical": "Our hospital is equipped with state-of-the-art surgical facilities.",
                "diagnostics": "We offer comprehensive diagnostic services, including X-ray, MRI, and lab tests."
            },
            "appointments": "To book an appointment, visit our website or call our appointment desk.",
            "billing": "You can pay your bills online or at the hospital's billing counter.",
            "support": "We provide patient assistance services, including interpreters and counseling.",
            "contact": "You can contact us at 123-456-7890 or email info@hospital.com."
        }

    def show_main_menu(self):
        print("Welcome to the Hospital Chatbot! How can I assist you today?")
        print("1. Hospital Overview")
        print("2. Facilities")
        print("3. Appointments")
        print("4. Billing Information")
        print("5. Support Services")
        print("6. Contact Information")
        print("0. Exit")
        
    def show_facilities_menu(self):
        print("Please choose a facility to learn more about:")
        print("1. Emergency Services")
        print("2. Outpatient Clinics")
        print("3. Inpatient Services")
        print("4. Surgical Facilities")
        print("5. Diagnostic & Imaging")
        print("0. Back to Main Menu")
        
    def handle_input(self, user_input):
        if user_input == "1":
            print(self.services["overview"])
        elif user_input == "2":
            self.show_facilities_menu()
            facility_input = input("Enter your choice: ")
            self.handle_facility_input(facility_input)
        elif user_input == "3":
            print(self.services["appointments"])
        elif user_input == "4":
            print(self.services["billing"])
        elif user_input == "5":
            print(self.services["support"])
        elif user_input == "6":
            print(self.services["contact"])
        elif user_input == "0":
            print("Thank you for using our chatbot. Goodbye!")
            return False
        else:
            print("Sorry, I didn't understand that. Please choose a valid option.")
        return True

    def handle_facility_input(self, facility_input):
        if facility_input == "1":
            print(self.services["facilities"]["emergency"])
        elif facility_input == "2":
            print(self.services["facilities"]["outpatient"])
        elif facility_input == "3":
            print(self.services["facilities"]["inpatient"])
        elif facility_input == "4":
            print(self.services["facilities"]["surgical"])
        elif facility_input == "5":
            print(self.services["facilities"]["diagnostics"])
        elif facility_input == "0":
            return  # Go back to the main menu
        else:
            print("Invalid option, please choose again.")

    def run(self):
        while True:
            self.show_main_menu()
            user_input = input("Enter your choice: ")
            if not self.handle_input(user_input):
                break

# Running the chatbot
if __name__ == "__main__":
    chatbot = HospitalChatbot()
    chatbot.run()
