import os
import window_viewport

exit_keys = ["exit", "quit", "q", "sair"]

def get_obj_path() -> str:
    while True:
        obj_name = input("Type your object name (e.g. cube.obj): ")
        file_path = os.path.join("models", obj_name)

        if obj_name in exit_keys:
            exit()
        elif not os.path.isfile(file_path):
            print(f"'{obj_name}' does not exist in the models folder.")
            print("")
        else: break
    
    return file_path

def set_point_of_view(choose: str):
    global window_viewport

    if choose == "y":    
        while True:
            window_viewport.u_max = input("Enter viewport width: ")
            if window_viewport.u_max in exit_keys:
                exit()
            elif not window_viewport.u_max.replace('.','',1).isdigit():
                print("Input must be a number.\n")
            else: 
                window_viewport.u_max = float(window_viewport.u_max)
                break
        
        while True:
            window_viewport.v_max = input("Enter viewport height: ")
            if window_viewport.v_max in exit_keys:
                exit()
            elif not window_viewport.v_max.replace('.','',1).isdigit():
                print("Input must be a number.\n")
            else: 
                window_viewport.v_max = float(window_viewport.v_max)
                break
        
        print("")
    else: print("")
    

def get_parameters():
    file_path = get_obj_path()
    print("")

    while True:
        choose = input("Do you want to choose the viewport size? [N/y]: ")
        if (choose in exit_keys): 
            exit()
        elif (choose.lower() == "n" or choose.lower() == "" or choose.lower() == "y"):
            set_point_of_view(choose.lower())
            break
        else:
            print("Invalid input.\n")

    return file_path