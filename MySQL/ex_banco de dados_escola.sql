
CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    serie VARCHAR(20),
    cidade VARCHAR(50),
    curso_id INT
);

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    carga_horaria INT
);

INSERT INTO alunos (nome, idade, serie, cidade, curso_id) VALUES
('Maria', 20, '2º ano', 'Curitiba', 2),
('João', 18, '1º ano', 'São Paulo', 3),
('Ana', 23, '3º ano', 'Curitiba', 1),
('Pedro', 21, '2º ano', 'Rio de Janeiro', 2),
('Lucas', 19, '1º ano', 'São Paulo', 4);

INSERT INTO cursos (nome, carga_horaria) VALUES
('Lógica de Programação', 40),
('Banco de Dados', 60),
('Desenvolvimento Web', 80),
('Python Básico', 50);


SELECT nome, cidade FROM alunos;

SELECT nome FROM cursos
WHERE carga_horaria > 50;

SELECT * FROM alunos
WHERE cidade = 'Curitiba';

SELECT nome, idade FROM alunos
WHERE idade < 22;

SELECT alunos.nome, cursos.nome
FROM alunos, cursos
WHERE alunos.curso_id = cursos.id;

SELECT alunos.nome
FROM alunos, cursos
WHERE alunos.curso_id = cursos.id
AND cursos.nome = 'Banco de Dados';

SELECT * FROM cursos
WHERE carga_horaria <> 60;

SELECT nome, cidade FROM alunos
WHERE cidade = 'São Paulo' OR cidade = 'Rio de Janeiro';
