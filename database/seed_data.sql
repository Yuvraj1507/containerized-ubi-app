INSERT INTO users (username, password_hash, email) 
VALUES ('admin', '$2b$12$hashedpassword123', 'admin@example.com');

INSERT INTO logs (user_id, action) 
VALUES (1, 'User admin created');
