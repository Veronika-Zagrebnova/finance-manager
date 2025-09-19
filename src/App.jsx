import { useEffect, useState } from 'react'
import './App.css'
import Entry from './components/Entry'
import UserEntry from './components/UserEntry'
import UserRegistry from './components/UserRegistry'
import axios from "axios"

function App() {

  const [entry, setEntry] = useState()
  const [isEntry, setIsEntry] = useState()
  console.log("App render")

  
 const shouldHideContent = isEntry === 'entry' || isEntry === 'registry'

  return (
    <>
    {!shouldHideContent && <Entry active={entry} onChange={(current) => setEntry(current)} />}

    {!shouldHideContent && entry == 'Entry' && <UserEntry active={isEntry} onChange={(current) => setIsEntry(current)}/>}

    {!shouldHideContent && entry == 'Registry' && <UserRegistry active={isEntry} onChange={(current) => setIsEntry(current)}/>}

    {isEntry == 'entry' && <div>Вы вошли</div>}
    {isEntry == 'registry' && <div>Регистрация завершена</div>}
    </>
  )
  
}

export default App