
import re

def analyze_java_code(code):
    classes = len(re.findall(r'class\s+\w+', code))
    methods = len(re.findall(r'(public|private|protected).*\(', code))
    imports = len(re.findall(r'import\s+', code))

    return {
        "classes": classes,
        "methods": methods,
        "imports": imports,
        "summary": f'This Java code contains {classes} classes, {methods} methods and {imports} imports. '
                   'The MVP demonstrates legacy code understanding and can be extended with RAG, '
                   'ChromaDB and Ollama.'
    }
