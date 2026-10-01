import type { RootState } from "@/app/model/store"
import { useSelector } from "react-redux"

export const useGlobalLoading = () => {
    return useSelector((state: RootState) => {
        const queries = Object.values(state.baseApi.queries || {})
        const mutations = Object.values(state.baseApi.mutations || {})

        const hasActiveQuery = queries.some(query => query?.status === 'pending');        
        const hasActiveMutation = mutations.some(mutation => mutation?.status === 'pending')

        return hasActiveQuery || hasActiveMutation
    })
}