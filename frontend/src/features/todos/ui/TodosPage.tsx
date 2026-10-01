import style from './TodosPage.module.css'
import { useForm } from "react-hook-form";
import { useAddTodoMutation, useDeleteTodoMutation, useGetTodosQuery, useUpdateTodoMutation } from "../api/todosApi"
import type { Todo } from '@/common/types';

export const TodosPage = () => {
    const { data } = useGetTodosQuery();
    const { register, handleSubmit, reset, formState: { errors } } = useForm();
    const [addTodo] = useAddTodoMutation();
    const [deleteTodo] = useDeleteTodoMutation();
    const [updateTodo] = useUpdateTodoMutation();

    const onSubmit = (data: any) => {
        addTodo(data)
            //без unwrap завжди буде спрацьовувати метод then, навіть якщо запит не вдалий
            .unwrap()
            .then(() => reset())
            .catch((error) => console.error(error));
    }

    const deleteTodoHandler = (id: number) => {
        deleteTodo(id)
            .unwrap()
            .catch((error) => console.error(error));
    }

    const updateTodoHandler = (todo: Todo) => {
        updateTodo({ id: todo.id, body: { ...todo, status: !todo.status } })
            .unwrap()
            .catch((error) => console.error(error));
    }

    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)} className={style.form}>
                <input 
                    placeholder='Назва задачі'
                    {...register("title", { required: true })} 
                    className={`${style.input} ${"title" in errors ? style.error : ''}`}
                />

                <input 
                    placeholder='Опис задачі'
                    {...register("description", { required: true })} 
                    className={`${style.input} ${"description" in errors ? style.error : ''}`}
                />
                <button className={style.button}>Відправити</button>
            </form>
            <div className={style.todosContainer}>
                {data?.map(todo => (
                <div key={todo.id} className={style.todoWrap}>
                    <h2>{todo.title}</h2>
                    <p>{todo.description}</p>
                    <p>{todo.status ? "Завершено" : "Не завершено"}</p>
                    <span
                        className={style.todoDelete}
                        onClick={() => updateTodoHandler(todo)}
                    >
                       {todo.status ? "✅" : "❌"}
                    </span>
                    <span
                        className={style.todoDelete}
                        onClick={() => deleteTodoHandler(todo.id)}
                    >
                       🗑️
                    </span>
                </div>))
            }
            </div>
        </div>
    )
}