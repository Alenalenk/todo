export type Todo = {
    id: number
    title: string
    description: string
    status: boolean
}

export type NewTodo = Omit<Todo, 'id'>