import { MainPage } from "@/app/ui/MainPage/MainPage"
import { TodosPage } from "@/features/todos/ui/TodosPage"
import { Route, Routes } from "react-router"
import { PageNotFound } from "../components/PageNotFound/PageNotFound"

export const Path ={
    Main: '/',
    Todos: '/todos',
    Profile: '/profile',
    NotFound: '*'
} as const

export const Routing = () => (
    <Routes>
        <Route path={Path.Main} element={<MainPage />} />
        <Route path={Path.Todos} element={<TodosPage />} />
        <Route path={Path.NotFound} element={<PageNotFound />} />
    </Routes>
)