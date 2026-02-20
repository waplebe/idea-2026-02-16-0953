import unittest
import main
import json

class TestMain(unittest.TestCase):

    def setUp(self):
        self.todo_file = "todo.json"
        self.initial_state = []

    def tearDown(self):
        if os.path.exists(self.todo_file):
            os.remove(self.todo_file)

    def test_load_tasks_empty_file(self):
        self.assertEqual(main.load_tasks(), [])

    def test_load_tasks_existing_file(self):
        with open(self.todo_file, "w") as f:
            json.dump(["Task 1", "Task 2"], f)
        self.assertEqual(main.load_tasks(), ["Task 1", "Task 2"])

    def test_save_tasks_empty_list(self):
        main.save_tasks([])
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            self.assertEqual(json.load(f), [])

    def test_save_tasks_with_tasks(self):
        tasks = ["Task 1", "Task 2"]
        main.save_tasks(tasks)
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            self.assertEqual(json.load(f), tasks)

    def test_add_task(self):
        main.add_task("New Task")
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            tasks = json.load(f)
            self.assertEqual(tasks, ["New Task"])

    def test_list_tasks(self):
        main.add_task("Task 1")
        main.add_task("Task 2")
        main.list_tasks()
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            tasks = json.load(f)
            self.assertEqual(tasks, ["Task 1", "Task 2"])

    def test_remove_task(self):
        main.add_task("Task 1")
        main.add_task("Task 2")
        main.remove_task("1")
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            tasks = json.load(f)
            self.assertEqual(tasks, ["Task 2"])

    def test_remove_task_invalid_number(self):
        main.add_task("Task 1")
        main.remove_task("1")
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            tasks = json.load(f)
            self.assertEqual(tasks, ["Task 1"])

    def test_remove_task_invalid_input(self):
        main.add_task("Task 1")
        main.remove_task("abc")
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            tasks = json.load(f)
            self.assertEqual(tasks, ["Task 1"])

    def test_load_tasks_invalid_json(self):
        with open(self.todo_file, "w") as f:
            f.write("This is not valid JSON")
        self.assertEqual(main.load_tasks(), [])

    def test_load_tasks_corrupted_json(self):
        with open(self.todo_file, "w") as f:
            f.write("[")  # Incomplete JSON
        self.assertEqual(main.load_tasks(), [])

    def test_load_tasks_empty_json(self):
        with open(self.todo_file, "w") as f:
            json.dump([], f)
        self.assertEqual(main.load_tasks(), [])

    def test_save_tasks_with_empty_list(self):
        main.save_tasks([])
        self.assertTrue(os.path.exists(self.todo_file))
        with open(self.todo_file, "r") as f:
            self.assertEqual(json.load(f), [])