from review_engine.llm_review import review_code_with_llm

sample_code = """
def greet(name):
    print("Hello " + name)

greet("Ritesh")
"""

result = review_code_with_llm("python", sample_code, debug=True)

if result["success"]:
    print("✅ AI Review:\n")
    print(result["response"])
else:
    print("❌ Error:\n", result["error"])
