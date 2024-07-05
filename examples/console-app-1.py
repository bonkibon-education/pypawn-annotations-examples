import pypawn_annotations

functions: tuple = (

    # Basic function params
    "native global_tag: function_name(tag: name = value)",
    "forward global_tag: function_name(tag: name = value)",
    "func global_tag: function_name(tag: name = value)"

    "native global_tag: function_name(const tag: name = value)",
    "forward global_tag: function_name(const tag: name = value)",
    "func global_tag: function_name(const tag: name = value)"

    # Hungarian notation | Auto-detect tag
    "func global_tag: function_name(iHungarianNotation = value)",
    "func global_tag: function_name(flHungarianNotation = value)",
    "func global_tag: function_name(szHungarianNotation = value)",
    "func global_tag: function_name(bHungarianNotation = value)"
)

if __name__ == "__main__":

    for line in functions:
        function = pypawn_annotations.PawnFunction(string=line)
        print(function.name)

        annotation = pypawn_annotations.Annotation(function=function, description=f'Description: {line}')
        print(annotation.show(), end="\n\n")
