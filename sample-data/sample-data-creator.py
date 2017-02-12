from faker import Factory
from datetime import datetime
import time
import random
milis = int(round(time.time() * 1000))
fake = Factory.create('en_US')
fake.seed(milis)

delimiter = ","

class Worker:
    def __init__(self, fake):
        self.fake = fake

    def create_worker(self, number):
        f = open("Worker.csv", 'w')
        first_id = 1
        for i in range(number):
            print >> f, self.__create_one_worker(first_id + i)
        f.close()

    def __create_one_worker(self, id):
        worker = ""
        worker += str(id)
        worker += delimiter
        first_name = self.fake.first_name()
        worker += first_name
        worker += delimiter
        last_name = self.fake.last_name()
        worker += last_name
        worker += delimiter
        worker += first_name + "." + last_name + "@gmail.com"
        return worker

class Project:
    def __init__(self, fake):
        self.fake = fake

    def create_project(self, number):
        f = open("Project.csv", 'w')
        start_id = 1
        for i in range (number) :
            print >> f, self.__create_one_project(start_id + i)
        f.close()

    def __create_one_project(self, id):
        project = ""
        project_name = fake.text(max_nb_chars=50)
        project += project_name
        project += delimiter
        project_code = project_name[0] + str(id)
        project += project_code
        return project


class ProjectUtils:
    def load_project_codes(self):
        project_codes = []
        linesRead = open("Project.csv", 'r+').read().splitlines()
        for line in linesRead:
            single_line_splited = line.split(delimiter)
            project_codes.append(single_line_splited[2])
        return project_codes

class TaskUtils:
    def loadTasks(self):
        task_ids = []
        lines_read = open("Task.csv", 'r+').read().splitlines()
        for line in lines_read:
            single_line_splited = line.split(delimiter)
            task_ids.append(single_line_splited[0])
        return task_ids

class MemberOfProject(ProjectUtils):
    def __init__(self, fake):
        self.fake = fake

    def create_member_of_project(self, number):
        project_codes = ProjectUtils.load_project_codes(ProjectUtils())
        f = open("MemberOfProject.csv", 'w')
        start_id = 1
        for i in range(number):
            randoms = [random.randint(1, project_codes.__len__() - 1) for _ in range(10)]
            for j in randoms:
                print >> f, self.__create_one_member_of_project(start_id + i, project_codes[j])
        f.close()

    def __create_one_member_of_project(self, worker_id, project_code):
        member_of_project = ""
        member_of_project += str(worker_id)
        member_of_project += delimiter
        member_of_project += str(fake.date_time_between_dates(datetime_start=datetime(2000, 1, 1),
                                                              datetime_end=datetime(2005, 1, 1)))[:10]
        member_of_project += delimiter
        member_of_project += str(fake.date_time_between_dates(datetime_start=datetime(2011, 1, 1),
                                                              datetime_end=datetime(2016, 1, 1)))[:10]
        member_of_project += delimiter
        member_of_project += project_code
        return member_of_project


class Task:
    def __init__(self, fake):
        self.fake = fake

    def create_task(self, number):
        project_codes = ProjectUtils.load_project_codes(ProjectUtils())
        f = open("Task.csv", 'w')
        start_id = 1
        for i in range(number):
            randoms = [random.randint(1, project_codes.__len__() - 1) for _ in range(10)]
            random_index = 0
            offset = 9
            for j in randoms:
                print >> f, self.__create_one_task(10 * (start_id + i) - offset + random_index, project_codes[j])
                random_index += 1
        f.close()

    def __create_one_task(self, id, projectCode):
        task = ""
        task += str(id)
        task += delimiter
        task_name = fake.text(max_nb_chars=50)
        task += task_name
        task += delimiter
        task += projectCode
        return task


class TimeReported:
    def __init__(self, fake):
        self.fake = fake

    def createTimeReported(self, number):
        project_codes = ProjectUtils.load_project_codes(ProjectUtils())
        task_ids = TaskUtils.loadTasks(TaskUtils())
        f = open("TimeReported.csv", 'w')
        start_id = 1
        for i in range(number):
            random_task_indexes = [random.randint(1, task_ids.__len__() - 1) for _ in range(10)]
            for j in random_task_indexes:
                random_project_indexes = [random.randint(1, project_codes.__len__() - 1) for _ in range(10)]
                for k in random_project_indexes:
                    print >> f, self.__create_one_time_reported(start_id + i, project_codes[k], task_ids[j])
        f.close()

    def __create_one_time_reported(self, workerId, projectCode, task_id):
        time_reported = ""
        time_reported += str(workerId)
        time_reported += delimiter
        time_reported += str(random.randint(1, 100))
        time_reported += delimiter
        time_reported += str(fake.date_time_between_dates(datetime_start=datetime(2006, 1, 1),
                                                          datetime_end=datetime(2010, 1, 1)))[:10]
        time_reported += delimiter
        time_reported += task_id
        return time_reported


Worker(fake).create_worker(1000)
Project(fake).create_project(1000)
MemberOfProject(fake).create_member_of_project(1000)
Task(fake).create_task(1000)
TimeReported(fake).createTimeReported(1000)
