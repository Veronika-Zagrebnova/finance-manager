
import Button from "./button"

export default function Entry({active, onChange}){
    return (
        <>
            <Button isActive={active=='Entry'} onClick={() => onChange('Entry')}>Войти</Button>
            <Button isActive={active=='Registry'} onClick={() => onChange('Registry')}>Зарегистрироваться</Button>
        </>
    )
    
}