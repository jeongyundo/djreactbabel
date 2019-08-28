import { combineReducers } from "redux";
import leads from "./leads";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  leads,
  errors,
  messages,
  auth
});

//리듀서에서 사용가능한 값들 추가