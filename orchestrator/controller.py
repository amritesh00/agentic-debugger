from agents.error_agent import detect_error
from agents.fix_agent import generate_fix
from agents.verify_agent import verify_solution
from rag.vector_store import search_docs

def run_debugger(code,error):

    explanation = detect_error(code,error)

    docs = search_docs(error)

    fix = generate_fix(code,error,docs)

    verification = verify_solution(fix)

    return explanation,fix,verification