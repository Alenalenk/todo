import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

const baseUrl = import.meta.env.VITE_BASE_URL;

export const baseApi = createApi({
    reducerPath: 'baseApi',
    tagTypes: ['Todo'],
    baseQuery: fetchBaseQuery({ baseUrl: baseUrl }),
    endpoints: () => ({})
})