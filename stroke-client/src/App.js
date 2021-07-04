import logo from './logo.svg';
import './App.css';
import {Container,Button,Form,Row,Col} from 'react-bootstrap'

function App()  {
  return (
    <Container  >
      <h1 style={{textAlign:"center"}}>Stroke Prediction web app </h1>
      <Form>
          <Form.Row>
            <Form.Group as={Col}>
              <Form.Label>Gender</Form.Label>
              <Form.Control as={'select'}>
                <option></option>
                <option>Male</option>
                <option>Female</option>
              </Form.Control>
            </Form.Group>
            <Form.Group as={Col}>
              <Form.Label>Age</Form.Label>
              <Form.Control/>
            </Form.Group>
          </Form.Row>
          <Form.Row>
            <Form.Group>
              <Form.Label>
                Hypertension
              </Form.Label>
            </Form.Group>
          </Form.Row>
      </Form>
    </Container>
   
  );
}

export default App;
