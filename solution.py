def a_project(projectID):
    supervisor =                                            #TO DO

    def the_project(request):
        nonlocal supervisor
        if request == "supervisor": return lambda: supervisor
        elif request == "set_supervisor": return set_sv
        elif request == "projectID": return                 #TODO
        else: return "the_project: unknown request " + request

    def project_supervisor(sv):
        nonlocal supervisor
        supervisor = sv
        return True

    return the_project

def project_supervisor(project):
    return project("supervisor")()

def set_supervisor(project, supervisor):
                                                            #TODO

def projectID(project):
                                                            #TODO
