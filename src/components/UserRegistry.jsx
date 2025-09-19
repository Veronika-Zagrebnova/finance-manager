import { useState } from "react"
import axios from "axios"


export default function UserRegistry({active, onChange}){

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isUserCreate, setIsUserCreate] = useState(false)
    const [isError, setIsError] = useState(false)

    function handleNameChange(event){
        setName(event.target.value)
    }

    function handleEmailChange(event){
        setEmail(event.target.value)
    }

    function handlePasswordChange(event){
        setPassword(event.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        const user = {email, password, name}
        console.log(user)
        axios.post('http://127.0.0.1:8000/users', user).then(r => {
            console.log('User create: ', r.data)
            setIsUserCreate(true)
            onChange('registry')
        }).catch(err => {
            console.log('err: ', err)
            setIsError(true)
        })
    }

    return(
        <>
            <h1>Зарегистрируйтесь</h1>

                <form onSubmit={handleSubmit}>
                    <label htmlFor="name">Имя</label>
                    <input type="text" id="name" name="name" value={name} onChange={handleNameChange} required />   

                    <label htmlFor="email">Email</label>
                    <input type="email" id="email" name="email" value={email} onChange={handleEmailChange} required />
            
                    <label htmlFor="psw">Пароль</label>
                    <input type="password" id="psw" name="psw" value={password} onChange={handlePasswordChange} required />

                    <button type="submit">Регистрация</button>
                </form>

            {isUserCreate == true && <>
                <p>{name}, вы зарегистрировались! Перейдите на страницу входа</p>
            </>}

            {isError == true && <>
                <p>Неправильно заполнены поля</p>
            </>}
        </>
    )
}