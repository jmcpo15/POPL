# Project Constructor
def a_project(projectID):
    supervisor = False

    def the_project(request):
        nonlocal supervisor
        if request == 'supervisor': return lambda: supervisor
        elif request == 'set_supervisor': return set_sv
        elif request == 'projectID': return projectID
        else: return "the_project: unknown request " + request

    def set_sv(sv):
        nonlocal supervisor
        supervisor = sv
        return True

    return the_project

def project_supervisor(project):
    return project("supervisor")()

def set_supervisor(project, supervisor):
    sv = supervisorID(supervisor)
    return project("set_supervisor")(sv)

def projectID(project):
    return project("projectID")

# Stduent Constructor

def a_student(studentID):
    student_project = False

    def the_student(request):
        nonlocal student_project
        if request == "allocation":
            if student_project == False: return False
            else: return student_project
        elif request == "studentID": return studentID
        elif request == "choose_project": return choose_project
        elif request == "drop_project": return drop_project
        else: return "the_student unkown request " + request

    def choose_project(projectID):
        nonlocal student_project
        if(student_project == False):
            student_project = projectID
            return True
        else: return False

    def drop_project():
        nonlocal student_project
        student_project = False
        return True

    return the_student

def allocation(student):
    return student("allocation")

def studentID(student):
    return student("studentID")

def choose_project(student, project):
    return student("choose_project")(project)

def drop_project(student):
    return student("drop_project")()

# Supervisor Constructor

def a_supervisor(supervisorID):
    quota = 6
    supervisor_projects = dict()

    def the_supervisor(request):
        nonlocal quota
        nonlocal supervisor_projects
        if request == "supervisorID": return supervisorID
        elif request == "quota": return quota
        elif request == "increment_quota": return increment_quota
        elif request == "decrement_quota": return decrement_quota
        elif request == "add_project": return add_project
        elif request == "allocate_project": return allocate_project
        elif request == "deallocate_project": return deallocate_project
        elif request == "list_allocated": return list_allocated_projects
        elif request == "list_available": return list_available_projects
        else: return "the_supervisor unkown request " + request

    def increment_quota():
        nonlocal quota
        quota += 1
        return True

    def decrement_quota():
        nonlocal quota
        if quota == 0:
            return False
        else:
            quota -= 1
            return True

    def add_project(project):
        nonlocal supervisor_projects
        supervisor_projects[project] = False

    def allocate_project(project, student):
        nonlocal supervisor_projects
        if project_supervisor(project) == supervisorID and supervisor_projects[project] == False and quota > 0:
            choose_project(student, project)
            decrement_quota()
            supervisor_projects[project] = student
            return True

    def deallocate_project(project, student):
        nonlocal supervisor_projects
        if project_supervisor(project) == supervisorID and supervisor_projects[project] != False:
            drop_project(student)
            increment_quota()
            supervisor_projects[project] = False
            return True

    def list_allocated_projects():
        nonlocal supervisor_projects
        list1 = []
        for project in supervisor_projects:
            if supervisor_projects[project] != False:
                proj = projectID(project)
                stud = studentID(supervisor_projects[project])
                list1.append((proj, stud))
        return list1

    def list_available_projects():
        nonlocal supervisor_projects
        list1 = []
        for project in supervisor_projects:
            if supervisor_projects[project] == False:
                list1.append(projectID(project))
        return list1

    return the_supervisor

def supervisorID(supervisor):
    return supervisor("supervisorID")

def quota(supervisor):
    return supervisor("quota")

def is_underloaded(supervisor):
    if quota(supervisor) == 0: return False
    else: return True

def increment_quota(supervisor):
    return supervisor("increment_quota")()

def decrement_quota(supervisor):
    return supervisor("decrement_quota")()

def add_project(supervisor, project):
    if project_supervisor(project) != False:
        return False
    else:
        set_supervisor(project, supervisor)
        supervisor("add_project")(project)
        return True

def allocate_project(supervisor, project, student):
    return supervisor("allocate_project")(project, student)

def deallocate_project(supervisor, project, student):
    return supervisor("deallocate_project")(project, student)

def list_allocated_projects(supervisor):
    return supervisor("list_allocated")()

def list_available_projects(supervisor):
    return supervisor("list_available")()


