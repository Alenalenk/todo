import style from './PageNotFound.module.css';

export const PageNotFound = () => {
    return (
        <div className={style.container}>
        <h1 className={style.title}>404</h1>
        <h2 className={style.subtitle}>Page Not Found</h2>
        </div>
    )
}