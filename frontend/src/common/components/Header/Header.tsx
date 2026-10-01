import { Path } from '@/common/routing';
import style from './Header.module.css'
import { NavLink } from "react-router";

const navItems = [
    { to: Path.Main, label: "Main" },
    { to: Path.Todos, label: "Todos" },
]

export const Header = () => {
    return (
        <header className={style.container}> 
            <nav>
                <ul className={style.list}>
                    {navItems.map(({ to, label }) => (
                        <li key={to} className={style.listItem}>
                            <NavLink
                                to={to}
                                className={({ isActive }) => `${style.link} ${isActive ? style.activeLink : ''}`}
                            >
                                {label}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </nav>
        </header>
    )
}   