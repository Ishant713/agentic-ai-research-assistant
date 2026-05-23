PLANNER_PROMPT = '''
Break the user query into 2 to 3 specific, concise research tasks.
Format: Output ONLY the tasks, one per line. Do not include any introduction, conclusion, numbering, bullet points, or markdown formatting.
Example input: Compare FastAPI and Express.js performance
Example output:
Benchmark FastAPI request response time
Benchmark Express.js request response time
Compare CPU and memory usage of FastAPI and Express.js
'''

RESEARCH_PROMPT = '''
Use web search and RAG context to generate research findings.
'''

SUMMARY_PROMPT = '''
Summarize the research findings into a coherent response.
'''

VALIDATOR_PROMPT = '''
Validate whether the answer is coherent and accurate.
If the answer is coherent and accurate, respond with 'APPROVED'. Otherwise, explain what is missing or incorrect in detail.
'''
