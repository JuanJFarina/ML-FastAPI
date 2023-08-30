import { useRef, useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const textRef = useRef(null);
  const [translation, setTranslation] = useState('');

  const getTranslation = () => {
    axios
      .post('https://ml-fast-api.vercel.app/translate?api_key=key123', {
        texto: textRef.current.value
      })
      .then(response => {
        if(response.data.idioma_original !== 'es') {
          setTranslation(response.data.traduccion);
        }
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
      <p>{translation}</p>
    </main>
  );
}

export default App;