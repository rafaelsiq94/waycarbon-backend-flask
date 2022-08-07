from flask import Blueprint, jsonify, request
from datetime import datetime
import uuid

from models.CarbonModel import CarbonModel
from models.entities.Carbon import Carbon
from utils.TcoFormat import TcoFormat

main = Blueprint("carbon_blueprint", __name__)


@main.route("/")
def get_carbons():
    try:
        carbons = CarbonModel.get_carbons()
        return jsonify(carbons)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_carbon(id):
    try:
        carbon = CarbonModel.get_carbon(id)
        if carbon != None:
            return jsonify(carbon)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_carbon():
    try:
        id = uuid.uuid4()
        creation_date = datetime.now()
        car_id = request.json["car_id"]
        km = request.json["km"]
        if car_id == 1:
            km_calc = km * 0.000166666666667
        elif car_id == 2:
            km_calc = km * 0.00025
        eletricity = request.json["eletricity"]
        eletricity_calc = eletricity * 0.000083333333333
        gas = request.json["gas"]
        gas_calc = gas * 0.040166666666667

        total_tco2_monthly = km_calc + eletricity_calc + gas_calc
        total_tco2_yearly = total_tco2_monthly * 12
        trees = int(total_tco2_yearly / 0.16)

        carbon = Carbon(
            str(id),
            car_id,
            km,
            eletricity,
            gas,
            total_tco2_monthly,
            total_tco2_yearly,
            trees,
            creation_date,
        )

        affected_rows = CarbonModel.add_carbon(carbon)

        if affected_rows == 1:
            return (
                jsonify(
                    {
                        "total_tco2_mes": TcoFormat.convert_tco(total_tco2_monthly),
                        "total_tco2_ano": TcoFormat.convert_tco(total_tco2_yearly),
                        "arvores": trees,
                    }
                ),
                200,
            )
        else:
            return jsonify({"message": "Erro ao inserir registro."}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_carbon(id):
    try:
        carbon = Carbon(id)

        affected_rows = CarbonModel.delete_carbon(carbon)

        if affected_rows == 1:
            return jsonify(carbon.id)
        else:
            return jsonify({"message": "Nenhum registro deletado."}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_carbon(id):
    try:
        creation_date = datetime.now()
        car_id = request.json["car_id"]
        km = request.json["km"]
        if car_id == 1:
            km_calc = km * 0.000166666666667
        elif car_id == 2:
            km_calc = km * 0.00025
        eletricity = request.json["eletricity"]
        eletricity_calc = eletricity * 0.000083333333333
        gas = request.json["gas"]
        gas_calc = gas * 0.040166666666667

        total_tco2_monthly = km_calc + eletricity_calc + gas_calc
        total_tco2_yearly = total_tco2_monthly * 12
        trees = int(total_tco2_yearly / 0.16)

        carbon = Carbon(
            id,
            car_id,
            km,
            eletricity,
            gas,
            total_tco2_monthly,
            total_tco2_yearly,
            trees,
            creation_date,
        )

        affected_rows = CarbonModel.update_carbon(carbon)

        if affected_rows == 1:
            return (
                jsonify(
                    {
                        "total_tco2_mes": format(total_tco2_monthly, ".3f").replace(
                            ".", ","
                        ),
                        "total_tco2_ano": format(total_tco2_yearly, ".3f").replace(
                            ".", ","
                        ),
                        "arvores": trees,
                    }
                ),
                200,
            )
        else:
            return jsonify({"message": "Erro ao atualizar registro."}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
