import Title from "../components/atoms/Tittle";
import styled from "styled-components";
import Button from "../components/atoms/Button";
import { useState } from "react";

function Home() {
    const [texto, setTexto] = useState("");
    const [analisisLexico, setAnalisisLexico] = useState("");
    const [analisisSintactico, setAnalisisSintactico] = useState("");
    const [error, setError] = useState("");

    const handleBorrarAnalisisLexico = () => {
        setTexto("");
        setAnalisisLexico("");
        setError("");
    };

    const handleBorrarAnalisisSintactico = () => {
        setTexto("");
        setAnalisisSintactico("");
        setError("");
    };

    const handleAnalisisLexico = async () => {
        try {
            const response = await fetch("http://localhost:5000/lexico", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ textarea_content: texto }),
            });
    
            const data = await response.json();
            if (data.error) {
                setError(data.error);
            } else {
                const formattedData = data.tokens.map(token => `Línea ${token[0]}: Tipo ${token[2]}, Valor '${token[1]}'`).join("\n");
                setAnalisisLexico(formattedData);
                setError("");
            }
        } catch (error) {
            setError("Error de conexión con el servidor");
        }
    };

    const handleAnalisisSintactico = async () => {
        try {
            const response = await fetch("http://localhost:5000/sintactico", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ textarea_content: texto }),
            });
    
            const data = await response.json();
            if (data.error) {
                setError(data.error);
            } else {
                if (Array.isArray(data.sintactico)) {
                    const formattedData = data.sintactico.map(item => `Línea ${item[0]}: ${item[2]}, Valor '${item[1]}'`).join("\n");
                    setAnalisisSintactico(formattedData);
                    setError("");
                } else {
                    setAnalisisSintactico(data.sintactico);
                    setError("");
                }
            }
        } catch (error) {
            setError("Error de conexión con el servidor");
        }
    };    
    

    return ( 
        <StyledDivHome>
            <StyledDivHome2>
                <Title des="Inserta Código a Analizar"></Title>
                <StyledTextarea 
                    name="Texto" 
                    id="Texto" 
                    rows="10" 
                    cols="50" 
                    value={texto}
                    onChange={(e) => setTexto(e.target.value)} 
                />
            </StyledDivHome2>
            <StyledContainerAnalisis>
                <StyledContainerAnalisis2>
                    <StyledItem1>
                        <Button type="button" value="Análisis Léxico" handlerClick={handleAnalisisLexico} />
                        <Button type="button" value="Borrar" handlerClick={handleBorrarAnalisisLexico} />
                    </StyledItem1>
                    <StyledItem2>
                        <StyledTextarea 
                            name="AnalisisLexico" 
                            id="AnalisisLexico" 
                            rows="10" 
                            cols="50" 
                            value={analisisLexico} 
                            readOnly
                        />
                    </StyledItem2>
                </StyledContainerAnalisis2>
                <StyledContainerAnalisis2>
                    <StyledItem1>
                        <Button type="button" value="Análisis Sintáctico" handlerClick={handleAnalisisSintactico} />
                        <Button type="button" value="Borrar" handlerClick={handleBorrarAnalisisSintactico} /> 
                    </StyledItem1>
                    <StyledItem2>
                        <StyledTextarea 
                            name="AnalisisSintactico" 
                            id="AnalisisSintactico" 
                            rows="10" 
                            cols="50" 
                            value={analisisSintactico} 
                            readOnly
                        />
                    </StyledItem2>
                </StyledContainerAnalisis2>
                {error && <Error>{error}</Error>}
            </StyledContainerAnalisis>
        </StyledDivHome>
    );
}

const StyledDivHome=styled.div`
    height: 100vh;
    width: 100%;
    background-color: #b0a17c;
    display: grid;
    align-items: center;
    justify-content: center;
`

const StyledDivHome2=styled.div`
    display: grid;
    align-items: center;
    justify-content: center;
`

const StyledTextarea=styled.textarea`
    background-color: #dfdacd;
    resize: none;
    color: #000000;
    font-family: Inter;
    font-size: 1rem;
    height: 15em;
    font-family: Inter;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
`
const StyledContainerAnalisis = styled.div`
    display: grid;
    grid-template-columns: auto auto;
    gap: 50px;
    padding: 10px;
`

const StyledContainerAnalisis2 = styled.div`
    display: grid;
`

const StyledItem1 = styled.div`
    display: grid;
    grid-template-columns: auto auto;
    gap: 20px;
`
const StyledItem2 = styled.div`
    display: grid;
    grid-template-rows: auto;
`

const Error = styled.div`
    color: red;
`

export default Home;
