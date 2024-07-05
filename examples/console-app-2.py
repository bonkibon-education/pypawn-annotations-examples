import pypawn_annotations

functions: tuple = (
    "native any: function@settings_get_cvar_args(const szKey[]);",
    "native bool: function@set_player_subclass_next(const iPlayer, const ApiClass: iClass, const ApiSubclass: iNewSubclass);",
    "native bool: function@set_player_subclass_current(const iPlayer, const ApiClass: iClass = API_CLASS_AUTO, const ApiSubclass: iSubclass = API_SUBCLASS_AUTO);",
    "native ApiSubclass: function@get_player_subclass(const iPlayer, const ApiClass: iClass, const ApiClassesState: iClassesState = API_CLASSES_STATE_CURRENT);",
    "native function@set_player_subclass(const ApiClass: iClass, const ApiSubclass: iSubclass, const ApiClassesState: iClassesState = API_CLASSES_STATE_CURRENT);",
)

if __name__ == "__main__":

    for line in functions:
        function = pypawn_annotations.PawnFunction(string=line)
        print(function.name)

        annotation = pypawn_annotations.Annotation(function=function, description=f"Description: {line}")
        print(annotation.show(), end="\n\n")
