# utils/prompt_templates.py
goal_template = """
You are helping a data scientist write a SMART goal for their performance evaluation.

Input: {input_text}

Instructions:
- Rephrase the input into a clear, concise, and measurable goal.
- Align it with professional growth or team outcomes.
- Use an encouraging and professional tone.
- Keep the goal specific, actionable, and realistic.

Return only the rewritten goal paragraph.
"""

achievement_template = """
You are helping a data scientist draft a self-evaluation statement describing their key achievements.

Input: {input_text}

Instructions:
- Convert bullet points or rough notes into a polished paragraph.
- Use strong, active language.
- Emphasize impact, innovation, and collaboration.
- Keep the tone confident and professional.

Return only the rewritten achievement paragraph.
"""

justification_template = """
You are writing a self-justification for a performance rating in a data scientist's performance evaluation.

Rating: {rating}
Input: {input_text}

Instructions:
- Write a paragraph justifying why this rating is appropriate.
- Highlight accomplishments, challenges overcome, and contributions.
- Use positive and evidence-based language.
- Keep it concise and professional.

Return only the justification paragraph.
"""

job_knowledge_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Job Knowledge".
Highlight continuous learning, mastery of duties, integration of ideas, and holistic thinking.
"""

service_excellence_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Service Excellence".
Demonstrate respect, empathy, exceptional service, and alignment with FIU's strategic goals.
"""

compliance_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Compliance and Accountability".
Highlight compliance with laws and policies, training completion, and integrity.
"""

communication_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Communication and Interpersonal Skills".
Demonstrate effective communication, listening, collaboration, and cultural awareness.
"""

efficiency_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Efficiency".
Showcase resource optimization, systems thinking, technology use, and time management.
"""

leadership_template = """
Input: {input_text}

Instructions:
Write a professional and polished self-evaluation paragraph based on the theme of "Management and Leadership".
Highlight supervision, recognition, alignment with goals, collaboration, and integrity.
"""
