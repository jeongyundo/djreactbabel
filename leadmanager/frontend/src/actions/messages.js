import { CREATE_MESSAGE, GET_ERRORS } from "./types";

// CREATE MESSAGE
export const createMessage = msg => {
  return {
    type: CREATE_MESSAGE,
    payload: msg
  };
};
//타입과 페이로드를통해 create_message와 메시지를 추가

// RETURN ERRORS
export const returnErrors = (msg, status) => {
  return {
    type: GET_ERRORS,
    payload: { msg, status }
  };
};
//타입과 페이로드를통해 get_errors와 메시지를 입력
//error가 한 종류로 발생하는 것이 아니라 여러 종류가 발생하기 때문 
