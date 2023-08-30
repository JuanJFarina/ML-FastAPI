import { useRef, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const textRef = useRef(null);
  const [translation, setTranslation] = useState('');
  const [answer, setAnswer] = useState('');

  const getTranslation = () => {
    setTranslation('');
    axios
      .post('https://ml-fast-api.vercel.app/translate?api_key=key123', {
        texto: textRef.current.value
      })
      .then(response => {
        if(response.data.idioma_original !== 'es') {
          setTranslation(`You said "${response.data.traduccion}" in spanish`);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const getSentiment = () => {
    setAnswer('');
    axios
      .post('https://ml-fast-api.vercel.app/analyze?api_key=key123', {
        texto: textRef.current.value
      })
      .then(response => {
        if(response.data.sentimiento === 'positivo') {
          setAnswer('Nos alegramos muchísimo que hayas tenido una grata experiencia !');
        }
        else if(response.data.sentimiento === 'negativo') {
          setAnswer('Lo lamentamos mucho ! Esperamos nos des otra oportunidad :(');
        }
        else {
          setAnswer('Muchas gracias por tu respuesta !');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const handleSubmit = () => {
    getTranslation();
    getSentiment();
  }

  return (
    <main>
      <h2>Hola ! Nos encantaría que nos dejes un comentario sobre nuestro servicio :)</h2>
      <h6>PS: please leave us a message, it doesn't matter if you don't know Spanish, we will translate it for you !</h6>
      <textarea ref={textRef} /><br />
      <input type="button" value="Enviar" onClick={handleSubmit} />
      <p>{translation}</p>
      <h3>{answer}</h3>
    </main>
  );
}

export default App;