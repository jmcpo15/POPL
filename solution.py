def a_project(projectID):
    supervisor = "John"                                           #TO DO

    def the_project(request):
        nonlocal supervisor
        if request == "supervisor": return lambda: supervisor
        elif request == "set_supervisor": return set_sv
        elif request == "projectID": return projectID                #TODO
        else: return "the_project: unknown request " + request

    def project_supervisor(sv):
        nonlocal supervisor
        supervisor = sv
        return True

    return the_project

def project_supervisor(project):
    return project("supervisor")()

def set_supervisor(project, supervisor):

	return project                                                            #TODO

def projectID(project):
        return project                                                    #TODO



def a_student(stduentID):
	return the_studnet



def a_supervisor(supervisorID):
	return supervisorID


pro = a_project("TTT")
print(pro("John"))
