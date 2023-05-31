USE todo_db_list;

CREATE TABLE todolist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
);
