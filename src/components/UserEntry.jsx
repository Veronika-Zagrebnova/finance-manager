import { useState } from "react"
import axios from "axios"


export default function UserEntry({active, onChange}){

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    function handleEmailChange(event){
        setEmail(event.target.value)
    }
    function handlePassworsChange(event){
        setPassword(event.target.value)
    }


    const handleSubmit = (e) => {
        e.preventDefault()
        const user = {email, password}
        console.log(user)
        axios.post('http://127.0.0.1:8000/get-user', user).then(r => {
            onChange('entry')
            console.log('User : ', r.data)
        }).catch(err => {
            console.log('err: ', err)
        })
    }
 
    return(
 
        <div className="enter" id="enter">
            <h1>Войдите в учетную запись пользователя</h1>
    
            <form onSubmit={handleSubmit}>
              <label htmlFor="email">Email</label>
              <input type="email" id="email" name="email" value={email} onChange={handleEmailChange} required />
            
              <label htmlFor="psw">Пароль</label>
              <input type="password" id="psw" name="psw" value = {password} onChange={handlePassworsChange} required />
              <button type="submit">Вход</button>
 
            </form>
        </div>
    )
    
}