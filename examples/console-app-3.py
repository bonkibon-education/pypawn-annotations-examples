import pypawn_annotations

test_natives: tuple = (
    'function(',
    'function()',
    'native function(',
    'native function()',
    'native tag: function()',
    'native tag: tag: function()',
    'native native tag: function()',
    'native tag: function(arg)',
    'native tag: function(const arg)',
    'native tag: function(const bool: arg)',
    'native tag: function(const bool: bIs)',
    'native !&(* bool: function(const bool: bIs)',
    'native !&(* Tag:&!*#$%: function(const bool: bIs = false, const szArray[32], const int iInt=30)',
    'native !&(* Tag:&!*#$%: bool:@&*(*&FDJKH!&*(const bool: bIs = false, const szArray[32] = "", const int iInt=30)',
    'forward f@$*!. Tag:&!*#$%: bool:@&*(*&FDJKH!&*()((const bool: bIs = false, const szArray[32] = "", const int iInt=30))',
)


if __name__ == "__main__":

    for i, native in enumerate(test_natives):
        function: pypawn_annotations.PawnFunction = pypawn_annotations.PawnFunction(string=native)

        print(f"[{i}] string: {function.string}")
        print("\t[1] title:", function.title)
        print("\t[2] general_tag:", function.general_tag)
        print("\t[3] name:", function.name)
        print("\t[4] args:", function.args)
        print("\t[5] is_title_tag_function:", function.is_title_function())
        print("\t[7] is_title_tag_forward:", function.is_title_forward())
        print("\t[8] is_title_tag_native:", function.is_title_native())
        print("\t[8] flags:", function.flags())
        print()
        print(pypawn_annotations.Annotation(description=function.string, function=function).show())
        print("_" * 100)
