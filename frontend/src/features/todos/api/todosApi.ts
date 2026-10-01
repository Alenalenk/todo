import { baseApi } from "@/app/api/baseApi";

export const todosApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        getTodos: build.query<any, void>({
            query: () => 'todos',
            providesTags: ['Todo']
        }),
        addTodo: build.mutation({
            query: (newTodo) => ({
                url: 'todos',
                method: 'POST',
                body: newTodo
            }),
            invalidatesTags: ['Todo']
        }),
        deleteTodo: build.mutation({
            query: (id) => ({
                url: `todos/${id}`,
                method: 'DELETE'
            }),
            invalidatesTags: ['Todo']
        }),
        updateTodo: build.mutation({
            query: ({ id, body }) => ({
                url: `todos/${id}`,
                method: 'PUT',
                body: body
            }),
            invalidatesTags: ['Todo']
        })
    })
})

export const { useGetTodosQuery, useAddTodoMutation, useDeleteTodoMutation, useUpdateTodoMutation } = todosApi


