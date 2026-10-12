
import { Routing } from '@/common/routing'
import style from './App.module.css'
import { Header } from '@/common/components'
import { useGlobalLoading } from '@/common/hooks'

function App() {

  const isLoading = useGlobalLoading()

  return (
    <>
      <Header />
      {isLoading && <div>Завантаження...</div>}
      <div className={style.layout}>
        <div className="@container">
          <Routing />
        </div>
      </div>
    </>
  )
}

export default App
