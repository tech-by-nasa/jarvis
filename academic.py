class AcademicGuide:
    @staticmethod
    def get_prompt(assignment_query):
        return f"""
        Act as an expert academic tutor (Claude-style). 
        Task: {assignment_query}
        Format your response as:
        1. UNDERSTANDING: Summarize the task.
        2. STRATEGY: Break this into 5 logical steps.
        3. EXECUTION: Draft the first section or provide a complex code snippet.
        4. CRITICAL FEEDBACK: What should the user watch out for?
        """
