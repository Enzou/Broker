import Html exposing (..)
import Html.App as App
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Http
import Json.Decode as Json
import Task



main =
    App.program
        { init = init "persons/1"
        , view = view
        , update = update
        , subscriptions = subscriptions
        }





-- MODEL


type alias Model = 
    { query: String
    , result: String
    }


init : String -> (Model, Cmd Msg)
init path =
    ( Model path "-"
    , getResponse path
    )


-- UPDATE


type Msg
    = QueryServer
        | FetchSucceed String
        | FetchFail Http.Error


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        QueryServer ->
            (model, getResponse model.query)

        FetchSucceed result ->
            (Model model.query result, Cmd.none)

        FetchFail _ ->
            (model, Cmd.none)



-- VIEW


view : Model -> Html Msg
view model =
    div []
        [ h2 [] [text model.query]
        , button [ onClick QueryServer ] [ text "Send Request" ]
        , br [] []
        , span [] [ text model.result ]
        ]



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none



-- HTTP


getResponse : String -> Cmd Msg
getResponse query =
    let
        url =
            "http://0.0.0.0:5000/api/" ++ query
    in
        Task.perform FetchFail FetchSucceed (Http.get parseResponse url)


parseResponse : Json.Decoder String
parseResponse =
    Json.at ["username"] Json.string

