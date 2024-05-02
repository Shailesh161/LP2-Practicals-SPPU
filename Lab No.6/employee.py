class PerformanceEvaluationExpertSystem:
    def __init__(self):
        self.quality_of_work = None
        self.productivity = None
        self.communication_skills = None
        self.teamwork = None
        self.initiative = None
        self.problem_solving = None
        self.attendance = None

    def set_evaluation_scores(self):
        print("Please rate the employee's performance on a scale of 1 to 10 for each parameter:")
        self.quality_of_work = int(input("Quality of Work: "))
        self.productivity = int(input("Productivity: "))
        self.communication_skills = int(input("Communication Skills: "))
        self.teamwork = int(input("Teamwork: "))
        self.initiative = int(input("Initiative: "))
        self.problem_solving = int(input("Problem Solving: "))
        self.attendance = int(input("Attendance: "))

    def evaluate_performance(self):
        total_score = self.quality_of_work + self.productivity + self.communication_skills + \
                      self.teamwork + self.initiative + self.problem_solving + self.attendance
        average_score = total_score / 7

        print("\nPerformance Evaluation:")
        print(f"Quality of Work: {self.quality_of_work}")
        print(f"Productivity: {self.productivity}")
        print(f"Communication Skills: {self.communication_skills}")
        print(f"Teamwork: {self.teamwork}")
        print(f"Initiative: {self.initiative}")
        print(f"Problem Solving: {self.problem_solving}")
        print(f"Attendance: {self.attendance}")
        print(f"\nTotal Score: {total_score}")
        print(f"Average Score: {average_score:.2f}")

        if average_score >= 7:
            print("Excellent performance!")
        elif 5 <= average_score < 7:
            print("Good performance.")
        else:
            print("Performance needs improvement.")

# Example usage:
expert_system = PerformanceEvaluationExpertSystem()
expert_system.set_evaluation_scores()
expert_system.evaluate_performance()
