import { useRef, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const textRef = useRef(null);

  const getTranslation = () => {
    axios
      .post('https://ml-fast-api.vercel.app/translate', {
        texto: textRef.current.value
      })
      .then(response => {
        console.log('Response:', response.data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
    <main>
      <h2>Hola ! Nos encantaría que nos dejes un comentario sobre nuestro servicio :)</h2>
      <h6>PS: if you don't know Spanish, please write in English or any other language, and we will translate it for you !</h6>
      <textarea ref={textRef} /><br />
      <input type="button" value="Enviar" onClick={getTranslation} />
    </main>
  );
}

export default App;